# now if a new payment id added the class PaymantProcessor needs to be changed
# Hence, it will violate the open close principle. Lets make the chage
from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.prices[i] * self.quantities[i]

        return total


class Payment(ABC):
    @abstractmethod
    def pay(self, security_code):
        pass


class DebitPayment(Payment):
    def __init__(self):
        self.type = "debit"

    def pay(self, security_code):
        print(f"payment type is {self.type}")
        print(f"Verifying security code: {security_code}")


class CreditPayment(Payment):
    def __init__(self):
        self.type = "credit"

    def pay(self, security_code):
        print(f"payment type is {self.type}")
        print(f"Verifying security code: {security_code}")


# Here I am adding a new payment type. But PayPal works with email address
# and not the security code


class PaypalPayment(Payment):
    def __init__(self):
        self.type = "paypal"

    def pay(self, email_address):
        print(f"payment type is {self.type}")
        print(f"Verifying email address code: {email_address}")


if __name__ == "__main__":
    order = Order()
    order.add_item("A", 10, 100)
    order.add_item("B", 10, 100)
    order.add_item("C", 10, 100)

    print(order.total_price())

    paypal_payment = PaypalPayment()
    paypal_payment.pay(email_address="some@abc")
