# from abc import ABC, abstractmethod
# class Drawable(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def resize(self, factor: float):
#         pass
#
# # Circle Class (partially implements Drawable)
# class Circle(Drawable):
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def draw(self):
#         print(f"Drawing a Circle with radius {self.radius}")
#
#     # resize() is not implemented, so Circle is a partial implementation of Drawable
#
# # ResizableCircle Class (fully implements Drawable)
# class ResizableCircle(Drawable):
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def draw(self):
#         print(f"Drawing a ResizableCircle with radius {self.radius}")
#
#     def resize(self, factor: float):
#         self.radius *= factor
#         print(f"Resized circle to radius {self.radius}")


# code has a violation of the Liskov Substitution Principle (LSP) because Circle does not fully implement Drawable. Here's why and how to fix it.
from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Resizable(Drawable):
    @abstractmethod
    def resize(self, factor: float):
        pass


class Circle(Drawable):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")


class ResizableCircle(Resizable):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self):
        print(f"Drawing a ResizableCircle with radius {self.radius}")

    def resize(self, factor: float):
        self.radius *= factor
        print(f"Resized circle to radius {self.radius}")
