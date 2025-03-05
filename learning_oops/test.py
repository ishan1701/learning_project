class Person:
    def __init__(self, name: str, age: int, url:str= 'dede'):
        self.name = name
        self._age = age
        self._url = url


    @property
    def age(self):
        return self.age

    @property
    def url(self):
        return self._url


    @property
    def person_details(self):
        return f'{self.name} is {self.age} years old. with his url: {self.url}'

    def __repr__(self):
        return f'{self.name} is created with {self.age} years old'

    def print(self):
        return f'{self.name} is {self.age} years old'


def main():
    p1 = Person('John', 20)

    print(p1.print())








if __name__ == '__main__':
    main()
