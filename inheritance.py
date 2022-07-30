class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        # self.__discount = 0.10  # private attribute
        self.__discount = None


    def set_discount(self, discount):
        self.__discount = discount


    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price


    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch


novel1 = Novel('Book 1', 1, 'John Doe', 120, 455)

novel1.set_discount(0.20)

academic1 = Academic('Book 2', 42, 'Silly Dolly', 120, 'Technology')


print(novel1)
print(academic1)

print("pages: ", novel1.pages)
print("branch: ", academic1.branch)


