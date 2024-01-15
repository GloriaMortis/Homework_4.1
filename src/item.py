class Item:

    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        total_price = self.price * self.quantity

        return total_price

    def apply_discount(self):
        self.price = self.price * self.pay_rate

        return self.price
