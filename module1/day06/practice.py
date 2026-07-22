# Day 06 Practice
# Day 06 Exercises — SOLID Principles

# Exercise 1: SRP (Single Responsibility Principle)
class ReportGenerator:
    def generate(self, data):
        return f"Report: {data}"

class ReportPrinter:
    def print_report(self, report):
        print(report)

generator = ReportGenerator()
printer = ReportPrinter()
report = generator.generate("Sales Data")
printer.print_report(report)


# Exercise 2: OCP (Open/Closed Principle)
class Discount:
    def apply(self, price):
        return price

class StudentDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class SeniorDiscount(Discount):
    def apply(self, price):
        return price * 0.8

discounts = [StudentDiscount(), SeniorDiscount()]
for d in discounts:
    print("Discounted price:", d.apply(100))


# Exercise 3: LSP (Liskov Substitution Principle)
class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"

class Eagle(Bird):
    def fly(self):
        return "Eagle soaring"

birds = [Sparrow(), Eagle()]
for b in birds:
    print(b.fly())


# Exercise 4: ISP (Interface Segregation Principle)
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_doc(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_doc(self):
        print("Printing document")

    def scan_doc(self):
        print("Scanning document")

mfp = MultiFunctionPrinter()
mfp.print_doc()
mfp.scan_doc()


# Exercise 5: DIP (Dependency Inversion Principle)
class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        print("Email:", message)

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

service = NotificationService(EmailSender())
service.notify("Hello via Email")
