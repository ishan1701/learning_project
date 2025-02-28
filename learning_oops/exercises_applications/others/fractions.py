class Fraction:
    def __init__(self, numerator, denominator):
        # Initialize the numerator and denominator properties
        # Check that the denominator is non-zero

        assert denominator != 0, f'denominator should be a non-zero value'
        self._numerator = numerator
        self._denominator = denominator

    @property
    def denominator(self):
        return self._denominator

    @property
    def numerator(self):
        return self._numerator

    @classmethod
    def add(cls, fraction1:'Fraction',fraction2:'Fraction'):
        return fraction1.add(fraction2)

    def add(self, other):
        # Add the current fraction and the other fraction
        # Return the result as a new Fraction object

        temp_fraction_1 = self.multiply(Fraction(other.denominator, other.denominator))
        temp_fraction_2 = other.multiply(Fraction(self.denominator, self.denominator))
        return Fraction(temp_fraction_1.numerator + temp_fraction_2.numerator, temp_fraction_1.denominator)

    def subtract(self, other):
        # Subtract the other fraction from the current fraction
        # Return the result as a new Fraction object
        temp_fraction_1 = self.multiply(Fraction(other.denominator, other.denominator))
        temp_fraction_2 = other.multiply(Fraction(self.denominator, self.denominator))
        return Fraction(temp_fraction_1.numerator - temp_fraction_2.numerator, temp_fraction_1.denominator)

    def multiply(self, other) -> 'Fraction':
        # Multiply the current fraction and the other fraction
        # Return the result as a new Fraction object
        result_number = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_number, result_denominator)

    def divide(self, other):
        # Divide the current fraction by the other fraction
        # Check that the other fraction has a non-zero numerator
        # Return the result as a new Fraction object
        if other.denominator == 0:
            raise ZeroDivisionError('division by zero')
        return self.multiply(Fraction(other.denominator, other.numerator))

    def simplify(self):
        # Simplify the current fraction to its simplest form
        # Return a new Fraction object with the simplified numerator and denominator
        numer_factors: set[int] = self.factors(self.numerator)
        denominator_factors: set[int] = self.factors(self.denominator)
        print(f'{numer_factors}')
        highest_common_factor = list(numer_factors.intersection(denominator_factors))[-1]
        return Fraction(int(self.numerator / highest_common_factor), int(self.denominator / highest_common_factor))

    @staticmethod
    def factors(number: int) -> set[int]:
        factors: set[int] = set()
        for i in range(1, number + 1):
            if number % i == 0:
                factors.add(i)
        return factors

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


def main():
    # Return the string representation of the fraction in the format "numerator/denominator"

    # Test your implementation
    fraction1 = Fraction(1, 4)
    fraction2 = Fraction(1, 2)

    fraction3 = fraction1.add(fraction2)
    print(fraction3)  # Should output "6/8"

    output_fraction=(Fraction.add(fraction1, fraction2))
    print(output_fraction)
    print(output_fraction.__class__.__name__)

    print(fraction1.multiply(fraction2))
    print(fraction1.subtract(fraction2))
    print(fraction1.divide(fraction2))

    fraction4 = fraction3.simplify()
    print(fraction4)  # Should output "3/4"


if __name__ == '__main__':
    main()


## THE BEST PART OF THIS PROGRAM IS add FUCTION IS ADDED BOTH AS CLASS METHOD AND INSTANCE METHOD.
## HENCE POLYMORPHISM