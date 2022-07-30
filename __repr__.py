class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price


    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


book1 = Book('Book 1', 12, 'John Doe', 120)
book2 = Book('Book 2', 42, 'Silly Dolly', 120)
book3 = Book('Book 3', 34, 'Snow Macker', 120)


print(book1)
print(book2)
print(book3)




