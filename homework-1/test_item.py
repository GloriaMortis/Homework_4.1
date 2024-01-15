class Test_Item:

    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Test_Item.all.append(self)

    def test_calculate_total_price(self) -> float:
        total_price = self.price * self.quantity

        return total_price

    def test_apply_discount(self):
        self.price = self.price * self.pay_rate

        return self.price


if __name__ == '__main__':
    item1 = Test_Item("apple", 100000, 4)

    #test 1
    assert item1.test_calculate_total_price()

    #test 2
    assert item1.test_apply_discount()

