from abc import ABC, abstractmethod

from components.memory import RAM
from components.processing_unit import CPU
from components.storage import Storage
from product.computer import Computer


class ComputerBuilder(ABC):
    @abstractmethod
    def assemble_memory(self, memory: RAM):
        pass

    @abstractmethod
    def assemble_storage(self, storage: Storage):
        pass

    @abstractmethod
    def assemble_processing_unit(self, processing_unit: CPU):
        pass

    @abstractmethod
    def get_product(self) -> Computer:
        pass
