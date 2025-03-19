from builders.computer_builder import ComputerBuilder
from product.computer import Computer
from abc import ABC, abstractmethod


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
        pass