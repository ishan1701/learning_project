from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"

# Step 1: Create an abstract Animal class
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age=age
    @abstractmethod
    def get_info(self) -> str:
        pass

# Step 2: Create concrete animal classes
class Dog(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context: dict):
        super().__init__(context["name"], context["age"])
    def get_info(self) -> str:
        return f"Dog {self.name} and age is {self.age}"

class Cat(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context: dict):
        super().__init__(context["name"], context["age"])
    def get_info(self) -> str:
        return f"Cat {self.name} and age is {self.age}"

class Fish(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context: dict):
        super().__init__(context["name"], context["age"])
    def get_info(self) -> str:
        return f"Fish {self.name} and age is {self.age}"

# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        animal_ref = {
            AnimalType.DOG: Dog,
            AnimalType.CAT: Cat,
            AnimalType.FISH: Fish
        }
        if animal_type not in animal_ref:
            raise NotImplementedError(f'Animal type {animal_type} not implemented')

        return animal_ref[animal_type](context=context)

# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    # Test the AnimalFactory by creating different types of animals and passing context data
    animal= animal_factory.create_animal(AnimalType.DOG, {'name':'dog', 'age':10})
    # print(animal.get_info())


if __name__ == "__main__":
    # main()
    print(AnimalType.DOG)