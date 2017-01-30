class Product:
    def __init__(self, name, price, item_number, details, image_url):
        self.name = name
        self.price = price
        self.item_number = item_number
        self.details = details
        self.image_url = image_url

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__str__() == other.__str__()
