
from abc import ABC, abstractmethod
from memory import DDR3, RAM
from storage import SSD, Storage
from processing_unit import IntelCPU, CPU

class Computer(ABC):
    def __init__(self, manufacturer: str, model: str, memory:RAM, storage: Storage, processing_unit: CPU, os:str):
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
        self.storage = storage
        self.processing_unit = processing_unit
        self.os = os

    @abstractmethod
    def is_graphics_card_supported(self) -> bool:
        pass

    @abstractmethod
    def is_game_supported(self) -> bool:
        pass

    @abstractmethod
    def if_new_os_supported(self, os:str) -> bool:
        pass

    def change_os(self, new_os: str):
        if self.if_new_os_supported(os=new_os):
            self.os = new_os
        else:
            print("OS not supported.")

class GamingComputer(Computer):
    def __init__(self):
        pass