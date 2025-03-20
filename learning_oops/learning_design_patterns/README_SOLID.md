
## classes and objects
1. While defining the class, we shud think if its a data oriented class or behavior oriented class.
2. classes are **nouns**. the best way to have a design.txt file before start coding and whaever Nouns we get, we should define the classes

## Encapsulation
In general a well defined class already achieve encapsulation in sense that it had captured all the 
relevant data and functionality. 
![img_3.png](uml/img_3.png)

For example 
An Apartment class is defined which should encapsulates the **Room class**.
So the room class should be defined before the Apartment class


## Inheritance

Inheritance allows us to GENERALIZE
a. Interface contracts

It defines a set of methods that needs to be implemented by any class that adheres the contract.
```
from abc import ABC, abstractmethod

# Interface (Abstract Base Class)
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Circle Class (implements Drawable)
class Circle(Drawable):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

# Rectangle Class (implements Drawable)
class Rectangle(Drawable):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a Rectangle with width {self.width} and height {self.height}")

# Example Usage
circle = Circle(5.0)
rectangle = Rectangle(4.0, 6.0)

shapes = [circle, rectangle]
for shape in shapes:
    shape.draw()
```
**Here the def draw method should be implemented in the child classes, because they are bind with the contract.
So child class and the parent class are bound to an inheritance contract.**


b. partially inheritance contracts
Refer to a concept where a class inherits only part of the behavior or properties from another class or interface, 
rather than fully implementing or extending it. 


Below is the code example

```
from abc import ABC, abstractmethod

# Interface (Abstract Base Class)
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor: float):
        pass

# Circle Class (partially implements Drawable)
class Circle(Drawable):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

    # resize() is not implemented, so Circle is a partial implementation of Drawable

# ResizableCircle Class (fully implements Drawable)
class ResizableCircle(Drawable):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self):
        print(f"Drawing a ResizableCircle with radius {self.radius}")

    def resize(self, factor: float):
        self.radius *= factor
        print(f"Resized circle to radius {self.radius}")

# Example Usage
circle = Circle(5.0)
circle.draw()  # Works
# circle.resize(1.5)  # This would raise an error since resize() is not implemented

resizable_circle = ResizableCircle(5.0)
resizable_circle.draw()  # Works
resizable_circle.resize(1.5)  # Works
```

However the above code violates the LSP of design patterns. because Circle does not fully implement Drawable. 
```angular2html

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
```

Here Circle is class which partially inherited where resize is not possible. **So the abstract method - resize is not implemented**
On the other hand, ResizableCircle is full inherited. **Hence all the abstract method should be implemented.**

Below is another example
```
from abc import ABC, abstractmethod

# Interface (Abstract Base Class)
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

    @abstractmethod
    def process_refund(self, amount: float):
        pass

# CreditCardProcessor (fully implements PaymentProcessor)
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount:.2f}")

    def process_refund(self, amount: float):
        print(f"Processing credit card refund of ${amount:.2f}")

# CashProcessor (partially implements PaymentProcessor)
class CashProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing cash payment of ${amount:.2f}")

    # process_refund() is not implemented, as cash refunds are not supported

# Example Usage
credit_card_processor = CreditCardProcessor()
credit_card_processor.process_payment(100.0)  # Works
credit_card_processor.process_refund(50.0)   # Works

cash_processor = CashProcessor()
cash_processor.process_payment(75.0)  # Works
# cash_processor.process_refund(25.0)  # This would raise an error since refunds are not supported
```

## UMLs for python OOPS


##  Interface contracts 

Its a concept that the abstract method must be implemented by the child classes. 

#### **SO THE ABSTRACT CLASS CANT BE INSTANTIATED. RATHER, IT is used FOR THE INTERFACE CONTRACTS**
```
from abc import ABC, abstractmethod

# Define the interface contract
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

# Implement the contract
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

# This will raise an error because `Square` does not implement `perimeter`
class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2
```

**So here the square and the circle needs to implement both area and perimeter method from the base class.**


##  Partial contracts
Lets suppose thre are 2 abstract methods declared in the Base classes.
However, it not mandatory that the child classes must implements both of the methods.
IF A CLASS HAS NOT IMPLEMENTED ALL THE ABSTRACT METHODS. THIS IS TERMED AS PARTIAL CONTRACTS.
SEE the EXAMPLES FOR CREDITCARD Previously.


# HallMark of the good architecture

SOLID principle of design pattens

#  Single responsibility(SRP):
 The classes, methods should do only a single thing. This helps the class or methods to be used very easily.
 **So each class should have a central responsibility**

### How to Apply SRP
**Identify Responsibilities:**

* Break down the functionality of a class into distinct responsibilities.

* If a class is doing more than one thing, split it into multiple classes.

**Delegate Responsibilities:**

* Use composition or dependency injection to delegate responsibilities to other classes.

**Avoid God Classes**:

* **A "God Class" is a class that does too much. Avoid creating such classes by adhering to SRP.**
```
class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        # Logic to generate the report
        return f"Report Data: {self.data}"

    def print(self):
        # Logic to print the report
        print(f"Printing Report: {self.generate()}")
```

* The Report class has two responsibilities: generating the report and printing it.

* If the printing logic changes, the Report class must be modified, even if the report generation logic remains the same.

```
class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        # Logic to generate the report
        return f"Report Data: {self.data}"

class ReportPrinter:
    def print(self, report):
        # Logic to print the report
        print(f"Printing Report: {report}")
```


Example in a Real-World Application
Imagine a user management system:

1. A User class might handle user data (e.g., name, email).

2. A UserValidator class might handle validation logic (e.g., checking if the email is valid).

3. A UserRepository class might handle database operations (e.g., saving the user to the database).

By separating these responsibilities, the system becomes more modular and easier to maintain.
# Open close principle or OCP
 classes should be open for extension rather than modification. The class modifications should be done very minimals 
Is means that you should be able to **add a new behaviour(extend functionality)** without modifying the existing code. 
It also means not to **alter the existing code** when adding a new functionality.

For example, the below code snippet 
```
class BillProcessor:
    def process_bill(self, bill_type, amount):
        if bill_type == "electricity":
            return amount * 1.1  # 10% tax for electricity
        elif bill_type == "water":
            return amount * 1.05  # 5% tax for water
        elif bill_type == "rent":
            return amount  # No tax on rent
        else:
            raise ValueError("Unknown bill type")

```
should be replaced with
```angular2html

class Bill(ABC):
    def __init__(self, amount):
        self.amount = amount
    @abstractmethod
    def calculate_bill(self):
        pass

# Concrete classes
class ElectricityBill(Bill):
## it ot required to add __init__ method if the parent and child has only one member which is defined in the parent class
    def calculate_total(self):
        return self.amount * 1.1  # 10% tax

class WaterBill(Bill):
    def calculate_total(self):
        return self.amount * 1.05  # 5% tax

class RentBill(Bill):
    def calculate_total(self):
        return self.amount  # No tax


class BillGeneratorFactory:
    @staticmethod 
    def create_bill(bill, amount):
        bill_classes= {
            'elec':ElectricityBill,
            'water':WaterBill
        }
        if bill in bill_classes:
            return bill_classes[bill](amount)


bill_object=BillGeneratorFactory.create_bill('water'.222)
bill_object.calculate_total()
    
```

* New bill types (e.g., InternetBill) can be added without modifying BillProcessor.
* Existing code remains untouched, reducing the risk of breaking things.
* Each bill type encapsulates its own logic, making the system more modular.

# Liskov Substitution Principle (LSP)

The child class should not change the expected behavior of the base class. Lets take an example
The subclasses should extend their base classes without changing their behavior.

```
class Bird:
    '''
    Purpose:
    '''
    def fly(self, altitude: float):
        print(f'Bird flying with altitude as {altitude}')


    def swim(self, deep: float):
        print(f'Bird swimming with deep {deep}')

class Sparrow(Bird):
    def swim(self, deep: float):
        print(f'Bird cant swim')

class Penguin(Bird):
    def fly(self, altitude: float):
        print('Penguin cant fly')


if __name__ == '__main__':
    p1=Penguin()
    p1.fly(233)  ## now this is a breaking change when I implement a Penguin class derived from the Bird class.


    sp1=Sparrow()
    sp1.fly(altitude=22.22)

    sp1.swim(1)## now this is a breaking change when I implement a Sparrow class derived from the Bird class.


Here is the correct way

class Bird:
    pass

class FlyingBird(Bird):
    def fly(self, altitude: float):
        print(f'Bird flying with altitude as {altitude}')

class SwimmingBird(Bird):
    def swim(self, deep: float):
        print(f'Bird swimming with deep {deep}')


class Sparrow(FlyingBird):
    pass

class Penguin(SwimmingBird):
   pass

class Duck(FlyingBird, SwimmingBird):
    pass

if __name__ == '__main__':
    sp1=Sparrow()
    sp1.fly(333) # here pon;y fly method is accessible from sp1

    d1=Duck()
    d1.swim(1)
    d1.fly(2323)  # both the methods are accessible

# Lets say I refactored the code as partial contracts

from abc import ABC, abstractmethod
class Bird:
    @abstractmethod
    def swim(self, depth:float):
        pass

    @abstractmethod
    def fly(self, height:float):
        pass



class Sparrow(Bird):
    def fly(self, height:float):
        print(f'Bird flying with deep {height}')

    def swim(self, height:float):
        print(f'cnt fky')



class Penguin(Bird):
    def swim(self, depth:float):
        print(f'Bird swimming with deep {depth}')

    def fly(self, height:float):
        print('cant fly')


if __name__ == '__main__':
    p1 = Penguin()
    p1.swim()


# HERE Penguin is forced to implement a method (fly) that it cannot logically support. The same with Sparrow class which is forced to implement the swim
#below is the correct implentation. It also violated the Interface segregation as Penguin class is forced to implement the fly method from the base class

from abc import ABC, abstractmethod

class Bird(ABC):  
    def eat(self): 
        print("Eating...")

class FlyingBird(Bird, ABC):  
    @abstractmethod
    def fly(self, height: float):
        pass

class SwimmingBird(Bird, ABC):  
    @abstractmethod
    def swim(self, depth: float):
        pass


class Sparrow(FlyingBird): 
    def fly(self, height: float):
        print(f'Sparrow flying at height {height} meters')


class Penguin(SwimmingBird):  
    def swim(self, depth: float):
        print(f'Penguin swimming at depth {depth} meters')



```

# Interface segregation
It means the client should not be forced to depend on the interface they **do not** use.
So the large interface with unrelated methods makes the code harder to maintain , extend and understand

The Interface Segregation Principle (ISP) states that a class should not be forced to implement methods it does not use. 
Instead of having one large, monolithic interface, we should create multiple smaller, more specific interfaces.



```angular2html

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor: float):  # ❌ Forces all shapes to be resizable
        pass

# ❌ Violates ISP because Circle does NOT need resize()
class Circle(Drawable):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

    def resize(self, factor: float):  # ❌ Circle shouldn't need this
        raise NotImplementedError("Circle cannot be resized")

```

The Drawable interface forces all shapes to implement both draw() and resize().

The refactored code should be
```angular2html
from abc import ABC, abstractmethod

# ✅ Now only contains drawing-related behavior
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# ✅ Separate interface for resizable objects
class Resizable(ABC):
    @abstractmethod
    def resize(self, factor: float):
        pass

# ✅ Circle only implements Drawable (NOT Resizable)
class Circle(Drawable):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

# ✅ Rectangle implements BOTH Drawable and Resizable
class ResizableRectangle(Drawable, Resizable):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a Rectangle with width {self.width} and height {self.height}")

    def resize(self, factor: float):
        self.width *= factor
        self.height *= factor
        print(f"Resized Rectangle to width {self.width} and height {self.height}")

# ✅ No unnecessary methods!
circle = Circle(5)
circle.draw()  # Works fine

rectangle = ResizableRectangle(10, 20)
rectangle.draw()
rectangle.resize(1.5)

```

# Dependency inversion

High-level modules should not depend on low-level modules. Both should depend on abstractions.

Abstractions should not depend on details. Details should depend on abstractions.

In simpler terms, DIP encourages designing systems where:

High-level modules (e.g., business logic) depend on abstractions (e.g., interfaces or abstract classes) rather than low-level modules (e.g., specific implementations).

Low-level modules also depend on the same abstractions, ensuring that both high-level and low-level modules are decoupled.

For eample the below code
```angular2html

class BillProcessor:
    def __init__(self, bill:Electricity): consider the bill as a concrete class
        self.bill = bill  # ❌ Directly depends on a concrete class

    def process(self):
        return self.bill.calculate_total()

```
1. BillProcessor is dependent on Electricity, violating DIP.
2. If we add Water bills, we must change BillProcessor, breaking Open/Closed Principle (OCP).


so here is the refactored code

```
from abc import ABC, abstractmethod

class Bill(ABC):  
    @abstractmethod
    def calculate_total(self):
        pass

class Electricity(Bill): 
    def calculate_total(self):
        return "Electricity Bill Processed"

class Water(Bill):  
    def calculate_total(self):
        return "Water Bill Processed"

class BillProcessor:
    def __init__(self, bill: Bill):  # BillProcessor depends on an abstraction, not a concrete class. The Base class is injested. Dependecny injection
        self.bill = bill

    def process(self):
        return self.bill.calculate_total()

# Injecting dependencies
electricity_bill = Electricity()
water_bill = Water()

processor1 = BillProcessor(electricity_bill)  # Injected Electricity
processor2 = BillProcessor(water_bill)  # Injected Water

print(processor1.process())  # Output: Electricity Bill Processed
print(processor2.process())  # Output: Water Bill Processed

```

We can also create Factory for Bills but the BillProcessor will perform the Dependency injections for base class
```
class BillFactory:
    @staticmethod
    def create_bill(bill_type: str, **kwargs) -> Bill:
        if bill_type.lower() == 'electricity':
            return Electricity(**kwargs)
        elif bill_type.lower() == 'water':
            return Water(**kwargs)
        elif bill_type.lower() == 'rental':
            return Rental(**kwargs)
        else:
            raise ValueError(f"Unknown bill type: {bill_type}")

class BillProcessor:
    def __init__(self, bill: Bill):
        self.bill = bill

    def process(self):
        return self.bill.calculate_total()


# Using the factory
bill = BillFactory.create_bill('electricity', amount=100, date="2025-02-24", bill_number="1234")
processor = BillProcessor(bill)
print(processor.process())

```

**Dependency Injection is one of the most common ways to implement the Dependency Inversion Principle.**

## Are design patterns are based on SOLID principles?

1. Yes, many design patterns are based on the SOLID principles or align well with them! While SOLID is a set of 
object-oriented design principles, design patterns are proven solutions to common design problems. 
In fact, a lot of design patterns are formulated to help achieve the goals of the SOLID principles, 
which aim to make software more modular, maintainable, flexible, and extensible.

2. Yes, design patterns are often based on or aligned with the SOLID principles. SOLID principles provide the 
foundational guidelines for designing clean, maintainable, and scalable object-oriented systems, 
while design patterns are proven solutions to common problems that arise when applying these principles in real-world scenarios.



## Relationship Between SOLID Principles and Design Patterns

1. Single Responsibility Principle (SRP)
SRP: Each class should have one responsibility (or reason to change).
Design Pattern Example: **Strategy Pattern.**
 The Strategy Pattern allows you to separate different behaviors (strategies) into separate classes, each with a single responsibility. This way, a class doesn't have to handle multiple behaviors.
 Example: Instead of having one class manage different sorting algorithms, each algorithm can be in its own class, and the main class can just choose which strategy (algorithm) to use.
2. Open/Closed Principle (OCP)
OCP: Classes should be open for extension but closed for modification.
Design Pattern Example: Decorator Pattern.
The Decorator Pattern allows you to add new behavior to objects without changing their code. This follows OCP because you're extending the functionality without modifying the original class.
Example: If you have a class that handles basic payment, you can add functionality like discounts or taxes using decorators without modifying the original payment class.
3. Liskov Substitution Principle (LSP)
LSP: Subtypes should be replaceable for their base types without affecting correctness.
Design Pattern Example: Factory Pattern.
The Factory Pattern creates objects without specifying the exact class of the object that will be created. The key idea is that all objects returned from the factory are interchangeable and can be used as the same base type.
Example: A factory might create either a Car or a Truck object. Both can be treated as Vehicle objects because they follow the same interface, ensuring Liskov Substitution.
4. Interface Segregation Principle (ISP)
ISP: Clients should not be forced to depend on interfaces they do not use.
Design Pattern Example: Adapter Pattern.
The Adapter Pattern helps in making a class conform to an interface that clients expect, without forcing them to use unnecessary methods.
Example: If a class has a large interface with many methods, you can use an adapter to create smaller, more specialized interfaces for clients to interact with, ensuring they only use what they need.
5. Dependency Inversion Principle (DIP)
DIP: High-level modules should not depend on low-level modules. Both should depend on abstractions.
Design Pattern Example: Dependency Injection.
Dependency Injection is a pattern where you inject the dependencies into a class instead of letting the class create them. This promotes DIP because the high-level class depends on an abstraction (interface), not on low-level details.
Example: Instead of creating a Database instance directly in your Service class, you inject a Database dependency, allowing you to easily swap it out with a different database implementation without modifying the Service class.
Summary of the Relationship
SOLID principles are guidelines for creating flexible and maintainable object-oriented code.
Design Patterns are solutions to common design problems that help implement these guidelines in practice.
Many design patterns are specifically created to help apply SOLID principles. They solve common issues like loose coupling, extensibility, and separation of concerns while adhering to SOLID principles.
So, when you use design patterns, you’re often implementing SOLID principles to create better software!



## when to use the Factory design pattern
1. When creating an object involves multiple steps, conditions, or dependencies (e.g., setting up defaults, validating inputs).
2. When the client specifies a type (e.g., "dell", "logitech") and the system decides which class to instantiate.
3. 