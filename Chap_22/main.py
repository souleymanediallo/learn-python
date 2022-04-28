import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity):

        assert price >= 0, f"Price {price} doit etre superieur ou egal à zero."
        assert quantity >= 0, f"Quantity {quantity} doit etre superieur ou egal à zero."

        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"

    def calculate_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    @classmethod
    def set_pay_rate(cls, amount):
        Item.pay_rate = amount

    @classmethod
    def format_product(cls):
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"


Item.format_product()
print(Item.all)
