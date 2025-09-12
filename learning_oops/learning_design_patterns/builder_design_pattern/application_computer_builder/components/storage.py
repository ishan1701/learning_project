from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, read_speed_mb: float, write_speed_mb: float, capacity: float):
        self.read_speed_mb = read_speed_mb
        self.write_speed_mb = write_speed_mb
        self.capacity = capacity

    @abstractmethod
    def read_data(self, file_path: str) -> None:
        pass

    @abstractmethod
    def write_data(self, file_path: str, data: bytes) -> bool:
        pass


class SSD(Storage):
    def __init__(
        self,
        read_speed_mb: float,
        write_speed_mb: float,
        capacity: float,
        interface: str,
    ):
        super().__init__(
            read_speed_mb=read_speed_mb,
            write_speed_mb=write_speed_mb,
            capacity=capacity,
        )
        self.interface = interface

    def read_data(self, file_path: str) -> None:
        print(f"Reading data from {file_path}")

    def write_data(self, file_path: str, data: bytes) -> bool:
        print(f"Writing data to {file_path}")
        return True
