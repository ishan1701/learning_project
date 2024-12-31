from dataclasses import dataclass, field
from typing import Any


def generate() -> list[str]:
    return ['a', 'b', 'c']


@dataclass(frozen=True) # this make sure that the class variables are immutable.
class Person:
    name: str
    age: int
    pet_names: list[str]
    email_address: list[str] = field(default_factory=list)
    another_generated_list: list[str] = field(default_factory=generate)# the generate function is declared up


if __name__ == '__main__':
    person_1 = Person(name='John', age=22, email_address=[], pet_names=[1, 2, 4])
    print(person_1)
    person_1.email_address.append('some')
    print(person_1)

    person_2 = Person(name='Simran', age=22, pet_names=[])

    print(person_2)
    person_2.pet_names.append(5)
    print(person_2)
    print(person_1)
    print(f'the pet_address of person_1 is {id(person_1.pet_names)}')
    print(f'the pet_address of person_2 is {id(person_2.pet_names)}')

    print(f'the email_address of person_1 is {id(person_1.email_address)}')
    print(f'the email_address of person_2 is {id(person_2.email_address)}')

    print(f'the email_address of person_1 is {id(person_1.another_generated_list)}')
    print(f'the email_address of person_2 is {id(person_2.another_generated_list)}')
    print(person_1.__eq__(person_2))
