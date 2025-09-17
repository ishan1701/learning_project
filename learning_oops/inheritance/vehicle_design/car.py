from vehicle_base import Vehicle


class Car(Vehicle):
    def __init__(self, max_speed: float, seating_capacity: int, model, color: str):
        super().__init__(max_speed=max_speed, color=color)
        self._seating_capacity = seating_capacity
        self._model = model

    @property
    def seating_capacity(self):
        return self._seating_capacity

    @property
    def model(self):
        return self._model

    def start(self):
        return f"car of model {self.model} is staring"

    def stop(self):
        return f"car of model {self.model} is stopping"

    @classmethod
    def create_object(cls, max_speed: float, color: str, **kwargs):
        return cls(
            max_speed=max_speed,
            seating_capacity=kwargs.get("seating_capacity"),
            model=kwargs.get("model"),
            color=color,
        )
