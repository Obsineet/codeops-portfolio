# Day 05 Practice
# Exercise 1: Animal base class
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())


# Exercise 2: Shape base class
import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rect = Rectangle(4, 6)
print("Circle area:", circle.area())
print("Rectangle area:", rect.area())


# Exercise 3: Polymorphism demonstration
shapes = [Circle(3), Rectangle(2, 5)]
for s in shapes:
    print("Area:", s.area())


# Exercise 4: Abstract Vehicle class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

vehicles = [Car(), Bike()]
for v in vehicles:
    print(v.drive())
