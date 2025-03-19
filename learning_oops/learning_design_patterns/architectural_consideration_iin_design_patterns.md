## Factory design pattern

Factory Method is a **creational** design pattern that provides an interface for creating objects in a superclass, 
but allows subclasses to alter the type of objects that will be created.
There are two variations of the factory design pattern. 
* Classic (ganf of 4)
* Simple Factory method which is more popular. Below is the architectural consideration


![img.png](images/img.png)
Builder is a **creational design pattern** that lets you construct complex objects step by step. 
The pattern allows you to produce different types and representations of an object using 
the same construction code.

* the client will only contact the factory to get the object of a concreate class
* in the factory class there will be a static method that will return the object of concreate class based on the input passed by the client
* There will be a switch/if-else in the factory method.
* Finally, **the client will never call the concreate classes methods. It only knows about the factory**

## Builder design pattern
The below uml is the combination of factory and builder.

```angular2html
+----------------+                                  +---------------------+
|    Director    |<>---------------------------->   |      Builder        | (Abstract)
+----------------+                                  +---------------------+
| - builder      |                                  | + buildFrame()      |
| + construct()  |                                  | + buildEngine()     |
+----------------+                                  | + buildExtras()     |
                                                    | + getResult(): Vehicle |
                                                     +---------------------+
                                                             ^
                                                             |
                                                     +---------------------+
                                                     | ConcreteBuilder     | (Abstract)
                                                     +---------------------+
                                                             ^
                                                             |
+-------------------+                                        |
| VehicleFactory <> |--------------------------------------->|                     
+----------------+  |                                        |
| + create_builder  |                                        |
(type: str): Builder|                                        |
+-------------------+                                        |
          |                            +----------------+   +----------------+   +----------------+
          |                            |   CarBuilder  |   |  BikeBuilder  |   |  ShipBuilder  |
          |                            +----------------+   +----------------+   +----------------+
          |                            | + buildFrame()|   | + buildFrame()|   | + buildFrame()|
          |                            | + buildEngine()|  | + buildEngine()|  | + buildEngine()|
          |                            | + buildExtras()|  | + buildExtras()|  | + buildExtras()|
          |                            | + getResult() |   | + getResult() |   | + getResult() |
          |                            +----------------+   +----------------+   +----------------+
          |                                     |                  |                  |
          v                                     v                  v                  v
+-----------------------------           +----------------+   +----------------+   +----------------+
|      Vehicle  | (Interface) |          |      Car       |   |      Bike      |   |      Ship      |
+-----------------------------|.         -----------------    ------------------   ------------------
| + get_details(): str        |          | - frame        |   | - frame        |   | - frame        |
|                             |          | - engine       |   | - engine       |   | - engine       |
|                             |          | - extras       |   | - extras       |   | - extras       |
|                             |          | + get_details()|   | + get_details()|  | + get_details() |
+----------------------------+           +----------------+   +----------------+   +----------------+
```

**As the number of components grows or their specificity varies across products 
(e.g., Car, Bike, Ship), cramming everything into build_extras() becomes 
messy and violates the Single Responsibility Principle. Making Director an abstract
class with concrete subclasses for each ConcreteBuilder is a solid approach to address
this—it allows each Director to tailor the construction process to its specific product’s needs**

```angular2html
+----------------+       +---------------------+
|    Director    | (Abstract)                |
+----------------+       +---------------------+
| - builder      |<>---->|      Builder        | (Abstract)
| + set_builder(builder: Builder)             |
| + construct(): Vehicle                      |
+----------------+       +---------------------+
          ^              | + buildFrame()      |
          |              | + buildEngine()     |
          |              | + getResult(): Vehicle |
          |              +---------------------+
          |                      ^
          |                      |
+----------------+   +----------------+   +----------------+
|   CarDirector  |   |  BikeDirector |   |  ShipDirector  |
+----------------+   +----------------+   +----------------+
| + construct()  |   | + construct()  |   | + construct()  |
+----------------+   +----------------+   +----------------+
          |                  |                  |
          v                  v                  v
+----------------+   +----------------+   +----------------+
|   CarBuilder  |   |  BikeBuilder  |   |  ShipBuilder  |
+----------------+   +----------------+   +----------------+
| + buildFrame()|   | + buildFrame()|   | + buildHull()  |
| + buildEngine()|  | + buildEngine()|  | + buildEngine()|
| + buildDoors()|   | + buildHandlebars()| + buildDeck()|
| + getResult() |   | + getResult() |   | + getResult() |
+----------------+   +----------------+   +----------------+
          |                  |                  |
          v                  v                  v
+----------------+   +----------------+   +----------------+
|      Vehicle  |<|--|      Car       |   |      Bike      |   |      Ship      |
| (Interface)   |    +----------------+   +----------------+   +----------------+
| + get_details()    | - frame        |   | - frame        |   | - hull         |
|                    | - engine       |   | - engine       |   | - engine       |
|                    | - doors        |   | - handlebars   |   | - deck         |
|                    | + get_details()|   | + get_details()|  | + get_details()|
+----------------+   +----------------+   +----------------+   +----------------+
```

