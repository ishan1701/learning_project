from abc import ABC, abstractmethod


class RAM(ABC):
    def __init__(self, capacity_in_gb: int, manufacturer: str, type: str, speed_range: int):
        self.capacity_in_gb = capacity_in_gb
        self.manufacturer = manufacturer
        self.type = type
        self.speed_range = speed_range

    @abstractmethod
    def upgrade_capacity(self, new_capacity: int) -> None:
        pass

    @staticmethod
    @abstractmethod
    def is_compatible_with_a_motherboard(motherboard: str) -> bool:
        pass


class DDR3(RAM):
    def __init__(self, capacity_in_gb: int, manufacturer: str, type: str, speed_range: int, latency):
        super().__init__(capacity_in_gb=capacity_in_gb, manufacturer=manufacturer, type=type, speed_range=speed_range)
        self.latency = latency

    @staticmethod
    def is_compatible_with_a_motherboard(motherboard: str) -> bool:
        if motherboard in ['a', 'b', 'c']:
            return True
        else:
            return False

    def upgrade_capacity(self, new_capacity: int) -> None:
        if self.latency > new_capacity:
            self.capacity_in_gb = new_capacity
