# The child class should not change the expected behavior of the base class.
#here the paypal payment is abusing the abstract method pay declared in parent class
from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

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
    def pay(self):
        pass


class DebitPayment(Payment):
    def __init__(self, security_code):
        self.type='debit'
        self.security_code = security_code

    def pay(self):
        print(f'payment type is {self.type}')
        print(f'Verifying security code: {self.security_code}')


class CreditPayment(Payment):
    def __init__(self, security_code):
        self.type='credit'
        self.security_code = security_code

    def pay(self):
        print(f'payment type is {self.type}')
        print(f'Verifying security code: {self.security_code}')


class PaypalPayment(Payment):
    def __init__(self, email_address):
        self.type = 'paypal'
        self.email_address = email_address

    def pay(self):
        print(f'payment type is {self.type}')
        print(f'Verifying email address code: {self.email_address}')
#
# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
#
# class SecureCodePayment(Payment):
#     @abstractmethod
#     def pay(self, security_code):
#         pass
#
# class SecureEmailPayment(Payment):
#     @abstractmethod
#     def pay(self, email_address):
#         pass
#
#
# class DebitPayment(SecureCodePayment):
#     def __init__(self):
#         self.type = 'debit'
#
#     def pay(self, security_code):
#         print(f'payment type is {self.type}')
#         print(f'Verifying security code: {security_code}')
#
#
# class CreditPayment(SecureCodePayment):
#     def __init__(self):
#         self.type = 'credit'
#
#     def pay(self, security_code):
#         print(f'payment type is {self.type}')
#         print(f'Verifying security code: {security_code}')
#
#
# class PaypalPayment(SecureEmailPayment):
#     def __init__(self):
#         self.type = 'paypal'
#
#     def pay(self, email_address):
#         print(f'payment type is {self.type}')
#         print(f'Verifying email address code: {email_address}')

# I TREID  THE ABOVE. BUT ITS WRONG .
# 1.In SecureCodePayment, pay() takes security_code as a parameter.
# In SecureEmailPayment, pay() takes email_address instead.
# This violates LSP because a common interface (Payment) should allow interchangeable usage of its derived classes.

# 2. Encapsulation of Specific Details
#
# Each subclass manages its own necessary details (e.g., security_code or email_address) inside the constructor.
# The pay() method remains uniform across all subclasses, allowing polymorphism to function smoothly.

if __name__ == '__main__':
    order = Order()
    order.add_item('A', 10, 100)
    order.add_item('B', 10, 100)
    order.add_item('C', 10, 100)

    print(order.total_price())

    paypal_payment = PaypalPayment(email_address='abc@somwe')
    paypal_payment.pay()

