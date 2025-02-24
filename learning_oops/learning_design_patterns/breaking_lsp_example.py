# class Bird:
#     '''
#     Purpose:
#     '''
#     def fly(self, altitude: float):
#         print(f'Bird flying with altitude as {altitude}')
#
#
#     def swim(self, deep: float):
#         print(f'Bird swimming with deep {deep}')
#
# class Sparrow(Bird):
#     def swim(self, deep: float):
#         print(f'Bird cant swim')
#
# class Penguin(Bird):
#     def fly(self, altitude: float):
#         print('Penguin cant fly')
#
#
# if __name__ == '__main__':
#     p1=Penguin()
#     p1.fly(233)  ## now this is a breaking change when I implement a Penguin class derived from the Bird class.
#
#
#     sp1=Sparrow()
#     sp1.fly(altitude=22.22)
#
#     sp1.swim(1)## now this is a breaking change when I implement a Sparrow class derived from the Bird class.


# Here is the correct way
#
# class Bird:
#     pass
#
# class FlyingBird(Bird):
#     def fly(self, altitude: float):
#         print(f'Bird flying with altitude as {altitude}')
#
# class SwimmingBird(Bird):
#     def swim(self, deep: float):
#         print(f'Bird swimming with deep {deep}')
#
#
# class Sparrow(FlyingBird):
#     pass
#
# class Penguin(SwimmingBird):
#    pass
#
# class Duck(FlyingBird, SwimmingBird):
#     pass
#
# if __name__ == '__main__':
#     sp1=Sparrow()
#     sp1.fly(333) # here pon;y fly method is accessible from sp1
#
#     d1=Duck()
#     d1.swim(1)
#     d1.fly(2323)  # both the methods are accessible

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


# HER`E Penguin is forced to implement a method (fly) that it cannot logically support. The same with Sparrow class which is forced to implement the swim
#below is the correct implentation

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


