class Category:
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__str__() == other.__str__()
