from abc import ABC, abstractmethod


class ElectronicDevice(ABC):
    @abstractmethod
    def battery_life(self):
        pass

    def type_of_device(self):
        return self.__class__.__name__

    ## THIS IS AN IMPLEMENTED METHOD


class Smartphone(ElectronicDevice):
    # Implement the battery_life method for the Smartphone class
    def battery_life(self):
        return "Smartphone battery life: 10 hours."


class Laptop(ElectronicDevice):
    # Implement the battery_life method for the Laptop class
    def battery_life(self):
        return "Laptop battery life: 5 hours."


class Smartwatch(ElectronicDevice):
    # Implement the battery_life method for the Smartwatch class
    def battery_life(self):
        return "Smartwatch battery life: 24 hours."


def display_battery_life(device: ElectronicDevice):
    # Call the battery_life method of the given device object and print the returned string\
    # MAKE AN ATTENTION THAT THE HINT TYPE IS OF THE BASE CLASS
    print(device.battery_life())


# Test your implementation
smartphone = Smartphone()
laptop = Laptop()
smartwatch = Smartwatch()

display_battery_life(smartphone)
display_battery_life(laptop)
display_battery_life(smartwatch)

print(smartwatch.type_of_device())
