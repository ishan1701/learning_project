from builders.computer_builder import ComputerBuilder
from builders.gaming_computer_builder import GamingComputerBuilder


class ComputerBuilderFactory:
    @staticmethod
    def builder_factory(
        product: str, manufacturer: str, model: str, os: str
    ) -> ComputerBuilder:
        if product == "gaming_pc":
            return GamingComputerBuilder(manufacturer=manufacturer, model=model, os=os)
        else:
            raise NotImplementedError("product must be gaming_pc")
