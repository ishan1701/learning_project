from pathlib import Path
from random import randint
from typing import Generator

from context import Context
from formatter_factory import TextFormatterStrategyFactory
from text_formatter import TextFormatter, TextFormatterTypeMap


def _read_file(file: Path) -> Generator[str, None, None]:
    with open(file) as f_read:
        for line in f_read:
            yield line


def _random_text_type() -> TextFormatterTypeMap:
    random_number = randint(1, 3)
    if random_number == 1:
        return TextFormatterTypeMap.TITLE
    elif random_number == 2:
        return TextFormatterTypeMap.UPPER
    else:
        return TextFormatterTypeMap.LOWER


if __name__ == "__main__":
    file_name = "sample.txt"
    file_path = Path(__file__).parent.parent.joinpath("data", file_name)
    contents = _read_file(file_path)

    with open(
        Path(__file__).parent.parent.joinpath("data", "output.txt"), "w+"
    ) as f_write:
        for content in contents:
            output_line: str = str()
            format_type = _random_text_type()
            text_formatter = TextFormatterStrategyFactory.formatter(
                formatter_type=format_type
            )
            context = Context(formatter=text_formatter)
            words = content.split(" ")
            for word in words:
                output_line += " ".join(context.run_formatter(text=word))

            f_write.write(output_line)

            f_write.write("\n")
