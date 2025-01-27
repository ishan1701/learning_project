from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, color:str, max_speed:float):
        self._color = color
        self._max_speed = max_speed

    @property
    def color(self):
        return self._color

    @property
    def max_speed(self):
        return self._max_speed


    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @classmethod
    @abstractmethod
    def create_object(cls, max_speed: float,color: str, **kwargs):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}(color={self._color}, max_speed={self._max_speed})'