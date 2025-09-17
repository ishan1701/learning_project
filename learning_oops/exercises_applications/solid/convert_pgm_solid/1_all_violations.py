# convet the below code to SOLID designed principle


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

    def pay(self, payment_type: str, security_code: str):
        if payment_type == "credit":
            print("payment type is credit")
            print(f"Verifying security code: {security_code}")

        elif payment_type == "debit":
            print("payment type is debit")
            print(f"Verifying security code: {security_code}")

        else:
            raise Exception("payment type is not valid")


if __name__ == "__main__":
    order = Order()
    order.add_item("A", 10, 100)
    order.add_item("B", 10, 100)
    order.add_item("C", 10, 100)

    print(order.total_price())
    order.pay("debit", "122")
