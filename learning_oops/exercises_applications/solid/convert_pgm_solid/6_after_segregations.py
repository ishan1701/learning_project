# now lets add a add new abstract method in payment to have 2-factor authentications
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
    def pay(self):
        pass


class PaymentProcessMultiFactor(Payment):
    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPayment(PaymentProcessMultiFactor):
    def __init__(self, security_code):
        self.is_multi_factor_auth = None
        self.type = "debit"
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        self.is_multi_factor_auth = True
        self.verified = True

    def pay(self):
        print(f"payment type is {self.type}")
        print(f"Verifying security code: {self.security_code}")


class CreditPayment(Payment):
    def __init__(self, security_code):
        self.type = "credit"
        self.security_code = security_code
        self.verified = False

    def pay(self):
        print(f"payment type is {self.type}")
        print(f"Verifying security code: {self.security_code}")


class PaypalPayment(PaymentProcessMultiFactor):
    def __init__(self, email_address):
        self.verified = None
        self.is_multi_factor_auth = None
        self.type = "paypal"
        self.email_address = email_address

    def auth_sms(self, code):
        self.is_multi_factor_auth = True
        self.verified = True

    def pay(self):
        print(f"payment type is {self.type}")
        print(f"Verifying email address code: {self.email_address}")


if __name__ == "__main__":
    order = Order()
    order.add_item("A", 10, 100)
    order.add_item("B", 10, 100)
    order.add_item("C", 10, 100)

    print(order.total_price())

    paypal_payment = PaypalPayment(email_address="abc@somwe")
    paypal_payment.pay()
