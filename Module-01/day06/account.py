# Addis Bank Account Project V3
# Addis Bank Account Class (V3) — SOLID + Design Patterns
from abc import ABC, abstractmethod

# --- SRP: Separate transaction logging ---
class TransactionLogger:
    def log(self, message):
        print("[LOG]", message)


# --- ISP: Interfaces for deposit, withdraw, report ---
class Depositable(ABC):
    @abstractmethod
    def deposit(self, amount): pass

class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, amount): pass

class Reportable(ABC):
    @abstractmethod
    def statement(self): pass


# --- DIP: Base Account depends on abstractions ---
class Account(Depositable, Withdrawable, Reportable, ABC):
    def __init__(self, owner, account_number, logger=None):
        self.owner = owner
        self.account_number = account_number
        self._balance = 0
        self.logger = logger or TransactionLogger()

    @property
    def balance(self):
        return self._balance

        if amount > 0:
            self._balance += amount
            self.logger.log(f"{self.owner} deposited {amount}")
        else:
            self.logger.log("Deposit must be positive.")

    @abstractmethod
    def withdraw(self, amount): pass

    @abstractmethod
    def statement(self): pass


# --- Strategy Pattern: Interest calculation ---
class InterestStrategy(ABC):
    @abstractmethod
    def calculate(self, balance): pass

class SimpleInterest(InterestStrategy):
    def __init__(self, rate=0.05):
        self.rate = rate
    def calculate(self, balance):
        return balance * self.rate

class NoInterest(InterestStrategy):
    def calculate(self, balance):
        return 0


# --- SavingsAccount with Strategy ---
class SavingsAccount(Account):
    def __init__(self, owner, account_number, interest_strategy=None, logger=None):
        super().__init__(owner, account_number, logger)
        self.interest_strategy = interest_strategy or SimpleInterest()

    def withdraw(self, amount):
        if amount <= 0:
            self.logger.log("Withdrawal must be positive.")
        elif amount > self._balance:
            self.logger.log("Insufficient funds.")
        else:
            self._balance -= amount
            self.logger.log(f"{self.owner} withdrew {amount}")

    def add_interest(self):
        interest = self.interest_strategy.calculate(self._balance)
        self._balance += interest
        self.logger.log(f"{self.owner} earned interest {interest}")

    def statement(self):
        print(f"Savings Account - Owner: {self.owner}, Balance: {self._balance}")


# --- CheckingAccount with overdraft ---
class CheckingAccount(Account):
    def __init__(self, owner, account_number, overdraft_limit=200, logger=None):
        super().__init__(owner, account_number, logger)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            self.logger.log("Withdrawal must be positive.")
        elif amount > self._balance + self.overdraft_limit:
            self.logger.log("Overdraft limit exceeded.")
        else:
            self._balance -= amount
            self.logger.log(f"{self.owner} withdrew {amount}")

    def statement(self):
        print(f"Checking Account - Owner: {self.owner}, Balance: {self._balance}")


   


# --- Demo ---
logger = TransactionLogger()

savings = SavingsAccount("Alice", "SAV123", interest_strategy=SimpleInterest(0.1), logger=logger)
savings.deposit(1000)
savings.add_interest()
savings.withdraw(200)
savings.statement()

checking = CheckingAccount("Bob", "CHK456", overdraft_limit=300, logger=logger)
checking.deposit(500)
checking.withdraw(700)  # allowed due to overdraft
checking.statement()
