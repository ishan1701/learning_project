from abc import ABC, abstractmethod

class Keyboard:

    def __init__(self, model, type, is_multilingual):
        self.model = model
        self.type = type
        self.is_multilingual = is_multilingual


class RechargeableKeyboard(Keyboard, ABC):
    def __init__(self, model, type, is_multilingual, battery_capacity: int):
        super().__init__(model=model, type =type, is_multilingual= is_multilingual,
                         )

        self._battery_hours = battery_capacity

    @property
    def battery_hours(self)-> int:
        return self._battery_hours

    @battery_hours.setter
    def battery_hours(self, value):
        self._battery_hours = value

    @abstractmethod
    def start_power(self, voltage:int) -> None:
        pass

class DellKeyboardRechargeable(RechargeableKeyboard):
    manufacturer = "Dell"

    def start_power(self, voltage:int) -> None:
        if voltage > 100:
            self.battery_hours = 10
        else:
            self.battery_hours = 5

