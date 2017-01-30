class Product:
    def __init__(self, name, discounted_price, high_price, item_number):
        self.name = name
        self.discounted_price = discounted_price
        self.high_price = high_price
        self.item_number = item_number

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__str__() == other.__str__()
