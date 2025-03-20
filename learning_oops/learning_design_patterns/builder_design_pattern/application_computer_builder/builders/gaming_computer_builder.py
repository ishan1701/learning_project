from components.keyboard import Keyboard
from builders.computer_builder import ComputerBuilder
from components.processing_unit import CPU
from components.storage import Storage
from components.memory import RAM
# from typing import Self
from product.computer import GamingComputer, Computer


class GamingComputerBuilder(ComputerBuilder):

    def __init__(self, manufacturer: str, model: str, os: str):
        self.keyboard = None
        self.memory = None
        self.storage = None
        self.processing_unit = None
        self.os = os
        self.graphics_card_memory = None
        self.manufacturer = manufacturer
        self.model = model

    def assemble_keyboard(self, keyboard: Keyboard) -> 'GamingComputerBuilder':
        self.keyboard = keyboard
        return self

    def assemble_memory(self, memory: RAM) -> 'GamingComputerBuilder':
        self.memory = memory
        return self

    def assemble_processing_unit(self, processing_unit: CPU) -> 'GamingComputerBuilder':
        self.processing_unit = processing_unit
        return self

    def assemble_storage(self, storage: Storage) -> 'GamingComputerBuilder':
        self.storage = storage
        return self

    def assemble_graphics_card_memory(self, graphics_card_memory: int) -> 'GamingComputerBuilder':
        self.graphics_card_memory = graphics_card_memory
        return self

    def get_product(self) -> Computer:
        return GamingComputer(manufacturer=self.manufacturer,
                              model=self.model,
                              memory=self.memory,
                              storage=self.storage,
                              processing_unit=self.processing_unit,
                              os=self.os,
                              graphics_card_memory=self.graphics_card_memory,
                              keyboard=self.keyboard)
