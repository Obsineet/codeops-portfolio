class Account:
    def init(self, owner, account_number, initial_balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = float(initial_balance) # Private balance attribute
        
    @property
    def balance(self):
        """Read-only property to access the encapsulated balance."""
        return self.__balance
        
    def deposit(self, amount):
        """Validate and execute a deposit."""
        if amount < 0:
            raise ValueError("Transaction failed: Negative deposits are rejected.")
        self.__balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        
    def withdraw(self, amount):
        """Validate and execute a withdrawal, preventing overdrafts."""
        if amount < 0:
            raise ValueError("Transaction failed: Negative withdrawals are not allowed.")
        if amount > self.__balance:
            raise ValueError("Transaction failed: Overdraft attempt blocked.")
        
        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")