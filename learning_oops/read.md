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
2. class level attribute  inside the class

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
question: why cls is the first param in the class method?


Answer- Because its being called by the class like `Person.from_string`. When the method is called by the onject like below
```angular2html
class Person:
    def some_method(self)

p=Person()
p.some_method
```
**In the above self is the first param in the method and in case of the class method it will be the cls as a param.**

4. static method

**In general, static methods are ideal for utility functions or logic that doesn't require access to either instance-level (self) or class-level (cls) data.**

```angular2html
class ApiOperator(BaseOperator):
    @staticmethod
    def handle_api_response(response):
        if response.status_code != 200:
            raise Exception(f"API call failed: {response.text}")
        return response.json()

class AnotherApiOperator(BaseOperator):
    def execute(self, context):
        response = call_some_api()
        data = ApiOperator.handle_api_response(response)
        self.log.info(f"Received data: {data}")

```
* Keeps utility functions logically grouped within the operator's scope.
* If you don't need access to the attributes or methods of the class or instance, a @staticmethod is better than a @classmethod or instance method. That way it is clear (from the @staticmethod decorator) that the class' and instance's state is not read or modified. However, using a function makes that distinction even clearer.

For example in the below
```angular2html
class Product:
    tax_rate = 0.1  # Class-level attribute
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @staticmethod
    def calculate_discount(price, discount_percentage):
        """
        Calculate the discounted price given a price and discount percentage.
        """
        return price - (price * discount_percentage / 100)


# Example Usage
price = 1200
discount = 10  # 10% discount
discounted_price = Product.calculate_discount(price, discount)
print(discounted_price)  # Output: 1080.0

```
here want to provide a utility to calculate discounts. This operation doesn’t depend on a specific product instance or the class itself but is related to products. A static method is perfect for this.



 @staticmethod is a method that belongs to the class itself but doesn't need access to instance data or class-level data. It’s used for functionality that is related to the class but doesn't need to access or modify the class state or instance state.


**IN SHORT 
THE CLASS METHOD IS GENERALLY USED TO CREATE THE OBJECTS

 
`
They are typically used to work with class-level data or to create instances of the class in a controlled manner (using factory methods or alternative constructors).
Static methods, on the other hand, can also be called on the class without an instance, but they don't have access to class-level or instance-level data.
So, if you need to interact with or modify class-level data or provide alternative ways to create class instances, class methods are the right tool for the job.**
`
![img.png](img.png)

An example is creating the objects from varios file types like yaml or json


# Encapsulations

Refers to mechanism to restring the direct access to some of the attributes. 
* creating a decorator and making the members as private is one of the way.
* making the members as private is also one of the way.
* It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. Encapsulation also restricts direct access to certain attributes or methods, providing controlled access via public methods (getters and setters).

**SO ONE OF THE USE CASE OF THE PROPERTY IS TO HIDE THE ACCESS OF THE OBJECTS(WHETHER ITS PROTECTED OF PRIVATE)**

# Abstraction
It defines to hide the necessary methods from the instances. For example 