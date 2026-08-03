# Day 04 Practice
# Exercise 1: Book class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

book1 = Book("Python Basics", "John Doe", 250)
print(book1.describe())


# Exercise 2: Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity  # private

    def restock(self, amount):
        self.__quantity += amount

    def sell(self, amount):
        if amount <= self.__quantity:
            self.__quantity -= amount
        else:
            print("Not enough stock!")

    @property
    def quantity(self):
        return self.__quantity

product1 = Product("Laptop", 1500, 5)
product1.sell(2)
print("Remaining:", product1.quantity)


# Exercise 3: Validate quantity never below zero
product2 = Product("Phone", 800, 3)
product2.sell(5)  # will print error
print("Remaining:", product2.quantity)


# Exercise 4: Multiple Product objects independence
product3 = Product("Tablet", 600, 10)
product4 = Product("Headphones", 200, 20)

product3.sell(2)
product4.restock(5)

print("Tablet quantity:", product3.quantity)
print("Headphones quantity:", product4.quantity)
