import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open(r'C:\Users\pouya\vsCodeProjects\PythonOOP-main\04 - Class vs Static Methods\codesnippets\items.csv', 'r') as f:
            
            reader = csv.DictReader(f)
            out = []
            # items = list(reader)
            for _ in range(5):
                out.append(next(reader))
            print(out)

    @classmethod
    def instantiate_from_csv2(cls):
        with open(r'C:\Users\pouya\vsCodeProjects\PythonOOP-main\04 - Class vs Static Methods\codesnippets\items.csv', 'r') as f:
            
            reader = csv.DictReader(f)
            items = list(reader)
            print(items)


Item.instantiate_from_csv()
Item.instantiate_from_csv2()

