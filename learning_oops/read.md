1. What is the use of assertion in Python?
When creating an object, you can use assert to ensure that the parameters passed to the constructor 
meet the required conditions.
```
class Person:
    def __init__(self, name, age):
        assert isinstance(name, str), "Name must be a string"
        assert age > 0, "Age must be positive"
        self.name = name
        self.age = age

# Example Usage
p1 = Person("Alice", 30)  # Works
p2 = Person("Bob", -5)    # Raises AssertionError: Age must be positive
```
2. global variables inside the class

3. class method
Scenario: I have a class which represents an Item. Now the requirement is to read the file and create the object by reading line by line.
**Here the class method can be used.**


Factory Methods can be defined using class method

Class methods are often used to create alternative constructors for a class. They allow the creation of objects in different ways than the standard __init__ constructor.

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_string):
        name, age = person_string.split(',')
        return cls(name, int(age))

person = Person.from_string("Alice,30")
print(person.name)  # Alice
print(person.age)   # 30
```

Singleton Pattern Implementation

Class methods can help implement the singleton pattern by ensuring only one instance of a class is created.

```
class Singleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

obj1 = Singleton.get_instance()
obj2 = Singleton.get_instance()
print(obj1 is obj2)  # True
```

4. static method