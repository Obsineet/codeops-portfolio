# Addis Bank Account Project V2
# Addis Bank Account Class (V2)
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit must be positive.")

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def statement(self):
        pass


class SavingsAccount(Account):
    def __init__(self, owner, account_number, interest_rate=0.05):
        super().__init__(owner, account_number)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount

    def add_interest(self):
        self._balance += self._balance * self.interest_rate

    def statement(self):
        print(f"Savings Account - Owner: {self.owner}, Balance: {self._balance}")


class CheckingAccount(Account):
    def __init__(self, owner, account_number, overdraft_limit=200):
        super().__init__(owner, account_number)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self._balance + self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            self._balance -= amount

    def statement(self):
        print(f"Checking Account - Owner: {self.owner}, Balance: {self._balance}")


# --- Demo ---
savings = SavingsAccount("Alice", "SAV123")
savings.deposit(1000)
savings.add_interest()
savings.withdraw(200)
savings.statement()

checking = CheckingAccount("Bob", "CHK456")
checking.deposit(500)
checking.withdraw(600)  # allowed due to overdraft
checking.statement()