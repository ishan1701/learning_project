from abc import ABC, abstractmethod
from product.computer import Computer
from components.memory import RAM
from components.storage import Storage
from components.processing_unit import CPU


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


