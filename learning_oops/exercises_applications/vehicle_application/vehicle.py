import logging
from abc import ABC, abstractmethod
from enum import Enum


# Step 0: Create an enumeration for vehicle types
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"


# Step 1: Create an abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class Car(Vehicle):
    def get_name(self) -> str:
        return "Car"


class Motorcycle(Vehicle):
    # Implement the get_name() method
    def get_name(self) -> str:
        return "Motorcycle"


class Bicycle(Vehicle):
    # Implement the get_name() method
    def get_name(self) -> str:
        return "Bicycle"


# Step 3: Create a VehicleFactory class
class VehicleFactory:
    def create_vehicle(self, vehicle_type: VehicleType) -> Vehicle:
        print(vehicle_type)

        vehicle_reference = {
            VehicleType.CAR: Car,
            VehicleType.BICYCLE: Bicycle,
            VehicleType.MOTORCYCLE: Motorcycle,
        }
        if vehicle_type not in vehicle_reference:
            raise ValueError(f"Vehicle type {vehicle_type} is not supported.")

        return vehicle_reference.get(vehicle_type)()


# Step 4: Test the VehicleFactory class
def main():
    vehicle_factory = VehicleFactory()

    # Test the VehicleFactory by creating different types of vehicles
    car = vehicle_factory.create_vehicle(VehicleType.CAR)
    print(car.get_name())

    motorcycle = vehicle_factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(motorcycle.get_name())

    bicycle = vehicle_factory.create_vehicle(VehicleType.BICYCLE)
    print(bicycle.get_name())


if __name__ == "__main__":
    main()
