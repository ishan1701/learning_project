from abc import ABC, abstractmethod

from components.keyboard import Keyboard
from components.memory import RAM
from components.processing_unit import CPU
from components.storage import Storage


class Computer(ABC):
    def __init__(
        self,
        manufacturer: str,
        model: str,
        memory: RAM,
        storage: Storage,
        processing_unit: CPU,
        os: str,
    ):
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
        self.storage = storage
        self.processing_unit = processing_unit
        self.os = os

    def __repr__(self):
        return f"{self.__class__.__name__}"

    @abstractmethod
    def is_graphics_card_supported(self) -> bool:
        pass

    @abstractmethod
    def is_game_supported(self) -> bool:
        pass

    @abstractmethod
    def if_new_os_supported(self, new_os: str) -> bool:
        pass

    def change_os(self, new_os: str):
        if self.if_new_os_supported(new_os=new_os):
            self.os = new_os
        else:
            print("OS not supported.")


class GamingComputer(Computer):
    def __init__(
        self,
        manufacturer: str,
        model: str,
        memory: RAM,
        storage: Storage,
        processing_unit: CPU,
        os: str,
        graphics_card_memory: int,
        keyboard: Keyboard,
    ):
        super().__init__(
            manufacturer=manufacturer,
            model=model,
            memory=memory,
            storage=storage,
            processing_unit=processing_unit,
            os=os,
        )
        self.graphics_card_memory = graphics_card_memory
        self.keyboard = keyboard

    def is_graphics_card_supported(self) -> bool:
        return True

    def if_new_os_supported(self, new_os: str) -> bool:
        if self.processing_unit.core > 2:
            return True
        else:
            return False

    def update_graphics_memory(self, new_graphics_memory):
        self.graphics_card_memory = new_graphics_memory

    def is_game_supported(self):
        return True


class Workstation(Computer):
    def __init__(
        self,
        manufacturer: str,
        model: str,
        memory: RAM,
        storage: Storage,
        processing_unit: CPU,
        os: str,
        alternate_os: str,
    ):
        super().__init__(
            manufacturer=manufacturer,
            model=model,
            memory=memory,
            storage=storage,
            processing_unit=processing_unit,
            os=os,
        )
        self.alternate_os = alternate_os

    def is_graphics_card_supported(self) -> bool:
        return False

    def if_new_os_supported(self, new_os: str) -> bool:
        if self.processing_unit.core > 4:
            return True
        else:
            return False

    def is_game_supported(self):
        return False


class Server(Computer):
    speed_range_for_heavy_computation = 12

    def __init__(
        self,
        manufacturer: str,
        model: str,
        memory: RAM,
        storage: Storage,
        processing_unit: CPU,
        os: str,
        vertically_scalable_capacity: int,
    ):
        super().__init__(
            manufacturer=manufacturer,
            model=model,
            memory=memory,
            storage=storage,
            processing_unit=processing_unit,
            os=os,
        )
        self.vertically_scalable_capacity = vertically_scalable_capacity

    def is_graphics_card_supported(self) -> bool:
        return False

    def if_new_os_supported(self, new_os: str) -> bool:
        if self.processing_unit.core > 6:
            return True
        else:
            return False

    def is_game_supported(self):
        return False

    def perform_heavy_computations(self):
        if self.memory.speed_range > self.speed_range_for_heavy_computation:
            print("Performing heavy computations...")
        else:
            print("Performing heavy can crash the server. Please upgrade")
