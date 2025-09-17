from car import Car
from truck import Truck


class VehicleFactory:
    @staticmethod
    def create_vehicles(
        vehicle_type, **kwargs
    ):  # trhis is thw factory method. However i
        if vehicle_type == "truck":
            return Truck(**kwargs)
        elif vehicle_type == "car":
            return Car(**kwargs)

        else:
            raise ValueError("Invalid vehicle type")
