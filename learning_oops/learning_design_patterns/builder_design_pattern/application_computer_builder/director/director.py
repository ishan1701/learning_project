from abc import ABC, abstractmethod

from builders.computer_builder import ComputerBuilder
from components.keyboard import Keyboard
from product.computer import Computer


class Director(ABC):
    def __init__(self, builder: ComputerBuilder, product: str):
        self._builder = builder
        self._product = product

    @property
    def builder(self) -> ComputerBuilder:
        return self._builder

    @property
    def product(self) -> str:
        return self._product

    @abstractmethod
    def build_computer(self, **kwargs) -> Computer:
        pass


class GameBuilderDirector(Director):
    def build_computer(self, **kwargs) -> Computer:
        (
            self.builder.assemble_keyboard(keyboard=kwargs["keyboard"])
            .assemble_memory(memory=kwargs["memory"])
            .assemble_storage(storage=kwargs["storage"])
            .assemble_graphics_card_memory(
                graphics_card_memory=kwargs["graphics_card_memory"]
            )
        )

        return self.builder.get_product()
