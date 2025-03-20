from abc import ABC, abstractmethod

class CPU(ABC):
    def __init__(self, model: str, core: int, cache_mb: int):
        self.model = model
        self.core = core
        self.cache_mb = cache_mb

    @staticmethod
    @abstractmethod
    def is_compatible_with_socket(self, socket_type: str) -> bool:
        pass


    @abstractmethod
    def get_speed(self, number_of_windows_opened:int) -> float:
        pass



class IntelCPU(CPU):
    def __init__(self, model: str, core: int, cache_mb: int):
        super().__init__(model, core, cache_mb)

    def get_speed(self, number_of_windows_opened:int) -> float:
        if number_of_windows_opened > 10:
            return self.core * 1.43
        else:
            return self.core * 2

    @staticmethod
    def is_compatible_with_socket(self, socket_type: str) -> bool:
        if socket_type in ['a', 'b', 'c']:
            return True
        else:
            return False


