from abc import ABC, abstractmethod
from typing import List, Dict
from pathlib import Path
import lkml
import os


# Strategy interfaces
class IDimensionStrategy(ABC):
    @abstractmethod
    def has_dimension(self, dimensions: List[Dict]) -> bool:
        pass


class IExploreValidationStrategy(ABC):
    @abstractmethod
    def validate(self, explore_content: Dict, views_to_check: List[str]) -> bool:
        pass


# Concrete strategies
class CountryDimensionStrategy(IDimensionStrategy):
    def has_dimension(self, dimensions: List[Dict]) -> bool:
        return any(d['sql'] == '${TABLE}.country' for d in dimensions)


class JoinValidationStrategy(IExploreValidationStrategy):
    def validate(self, explore_content: Dict, views_to_check: List[str]) -> bool:
        join_expression = os.environ.get('JOIN_EXPRESSION', '')
        for explore in explore_content.get('explores', []):
            for join in explore.get('joins', []):
                if join_expression in join.get('sql_on', ''):
                    return True
        return False


class AccessFilterValidationStrategy(IExploreValidationStrategy):
    def validate(self, explore_content: Dict, views_to_check: List[str]) -> bool:
        field = os.environ.get('ACCESS_FILTER_COUNTRY_PERMISSION_FIELD', '')
        for explore in explore_content.get('explores', []):
            for filter in explore.get('access_filters', []):
                if filter.get('field') == field and filter.get('user_attribute') == 'email':
                    return True
        return False


# Utility classes
class FileSeparator:
    @staticmethod
    def get_views(files: List[str]) -> List[str]:
        return [f for f in files if Path(f).suffix == '.lkml' and 'view' in Path(f).stem]

    @staticmethod
    def get_explores(files: List[str]) -> List[str]:
        return [f for f in files if Path(f).suffix == '.lkml' and 'explore' in Path(f).stem]


class LookMLReader:
    def __init__(self, project_root: Path):
        self.project_root = project_root

    def read(self, file_path: str) -> Dict:
        with (self.project_root / file_path).open('r') as f:
            return lkml.load(f)

    def scan_all_explores(self) -> List[Path]:
        return [p for p in self.project_root.rglob('*.explore.lkml')]


# Abstract Validator interface
class IValidator(ABC):
    def __init__(self, files: List[str], reader: LookMLReader):
        self.files = files
        self.reader = reader

    @abstractmethod
    def validate(self) -> None:
        pass


# Concrete validator implementations
class ViewCountryValidator(IValidator):
    def __init__(
            self,
            files: List[str],
            reader: LookMLReader,
            dim_strategy: IDimensionStrategy,
            explore_strategies: List[IExploreValidationStrategy]
    ):
        super().__init__(files, reader)
        self.dim_strategy = dim_strategy
        self.explore_strategies = explore_strategies
        self.view_files = FileSeparator.get_views(files)
        self.views_with_countries = []
        self.explores_to_validate = []

    def validate(self) -> None:
        self.find_views_with_countries()
        if not self.views_with_countries:
            print("No views with country dimensions found")
            return
        self.find_relevant_explores()
        self.validate_explores()

    def find_views_with_countries(self):
        for f in self.view_files:
            content = self.reader.read(f)
            if 'views' not in content or len(content['views']) != 1:
                raise KeyError("Invalid view file structure")
            if self.dim_strategy.has_dimension(content['views'][0].get('dimensions', [])):
                self.views_with_countries.append(f)
                print(f"View with country dimension: {f}")

    def find_relevant_explores(self):
        view_names = [Path(f).stem.replace('.view', '') for f in self.views_with_countries]
        for explore_file in self.reader.scan_all_explores():
            content = self.reader.read(explore_file.relative_to(self.reader.project_root).as_posix())
            for explore in content.get('explores', []):
                if explore.get('name') in view_names:
                    self.explores_to_validate.append(explore_file.as_posix())

    def validate_explores(self):
        if not self.explores_to_validate:
            print("No explores require validation")
            return
        for explore_file in self.explores_to_validate:
            content = self.reader.read(explore_file)
            for strategy in self.explore_strategies:
                if not strategy.validate(content, self.views_with_countries):
                    raise KeyError(f"Validation failed for {explore_file} with {strategy.__class__.__name__}")


class ExploresCountryValidator(IValidator):
    def __init__(
            self,
            files: List[str],
            reader: LookMLReader,
            dim_strategy: IDimensionStrategy,
            access_filter_strategy: IExploreValidationStrategy
    ):
        super().__init__(files, reader)
        self.dim_strategy = dim_strategy
        self.access_filter_strategy = access_filter_strategy
        self.explore_files = FileSeparator.get_explores(files)
        self.view_files_to_check = []

    def validate(self) -> None:
        if self.check_access_filters():
            print("All explores have valid access filters")
            return
        self.find_views_from_explores()
        self.check_views_for_dimensions()

    def check_access_filters(self) -> bool:
        for f in self.explore_files:
            content = self.reader.read(f)
            if not self.access_filter_strategy.validate(content, []):
                print(f"Access filter missing in {f}")
                return False
        return True

    def find_views_from_explores(self):
        for f in self.explore_files:
            content = self.reader.read(f)
            for explore in content.get('explores', []):
                view_name = explore.get('name')
                view_path = self.reader.project_root / 'views' / f"{view_name}.view.lkml"
                if view_path.exists():
                    self.view_files_to_check.append(view_path.as_posix())

    def check_views_for_dimensions(self):
        for f in self.view_files_to_check:
            content = self.reader.read(Path(f).relative_to(self.reader.project_root).as_posix())
            if self.dim_strategy.has_dimension(content['views'][0].get('dimensions', [])):
                raise ValueError(f"Country dimension found in {f} without access filter")


# Coordinator
class Validate:
    def __init__(self, files: List[str]):
        project_root = Path(__file__).parent.parent.parent.resolve()
        reader = LookMLReader(project_root)
        dim_strategy = CountryDimensionStrategy()
        explore_strategies = [JoinValidationStrategy(), AccessFilterValidationStrategy()]

        self.validators = [
            ViewCountryValidator(files, reader, dim_strategy, explore_strategies),
            ExploresCountryValidator(files, reader, dim_strategy, AccessFilterValidationStrategy())
        ]

    def run(self):
        for validator in self.validators:
            validator.validate()


# Usage
if __name__ == "__main__":
    files = ["views/file.view.lkml", "explores/file.explore.lkml"]
    validator = Validate(files)
    validator.run()