class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo", 122, 39.97)
b2 = Book("The Catcher in the Rye", "Soul", 122, 49.97)

# # TODO: print the price of book1
# b1 = b1.getprice()
# print(b1)

# TODO: try setting the discount
# print(b2.getprice())
# b2.setdiscount(0.25)
# print(b2.getprice())


# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)