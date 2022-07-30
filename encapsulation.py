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


singleBook = Book('Book 1', 1, 'John Doe', 120)
bulk_books = Book('Book 2', 42, 'Silly Dolly', 120)

bulk_books.set_discount(0.20)



print(singleBook.get_price())
print(bulk_books.get_price())
print(singleBook)
print(bulk_books)


