class BankAccount:
    """
    A class to represent a bank account.
    """
    # Class attribute (shared by all instances)
    bank_name = "Python National Bank"

    def __init__(self, owner_name, initial_balance=0):
        """
        The constructor method to initialize object attributes.
        It runs automatically when a new object is created.
        """
        self.owner = owner_name  # Instance attribute
        self.__balance = initial_balance  # Private attribute (encapsulation)
        print(f"Account created for {self.owner} at {BankAccount.bank_name}.")

    def deposit(self, amount):
        """
        Method to deposit funds into the account.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Method to withdraw funds from the account.
        Demonstrates conditional logic within an object's method.
        """
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")

    def get_balance(self):
        """
        Getter method to safely access the private balance attribute.
        """
        return self.__balance

    def __str__(self):
        """
        Special method to return a string representation of the object when printed.
        """
        return f"Account Owner: {self.owner}, Balance: ${self.__balance}"

# Inheritance Example: A specialized SavingsAccount class
class SavingsAccount(BankAccount):
    """
    A subclass that inherits from BankAccount and adds an interest rate feature.
    """
    def __init__(self, owner_name, initial_balance=0, interest_rate=0.01):
        super().__init__(owner_name, initial_balance) # Call the parent class constructor
        self.interest_rate = interest_rate
        print(f"Savings account created with interest rate of {self.interest_rate*100}%")

    def apply_interest(self):
        """
        A unique method for savings accounts to add interest.
        """
        interest_amount = self.__balance * self.interest_rate # Accessing the private attribute via inheritance scope
        self.deposit(interest_amount)
        print(f"Interest applied. Balance is now ${self.__balance}")

# --- Usage of the classes and objects ---

# 1. Create instances (objects) of the BankAccount class
print("--- Creating Standard Accounts ---")
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob") # Uses default balance of 0

# 2. Use object methods to perform actions
print("\n--- Performing Transactions ---")
account1.deposit(500)
account1.withdraw(200)
account2.deposit(50)
account2.withdraw(100) # Fails due to insufficient funds

# 3. Accessing information
print("\n--- Account Information ---")
# Using the __str__ method via print()
print(account1)
print(f"Bob's balance: ${account2.get_balance()}")

# 4. Create an instance of the derived class (Inheritance)
print("\n--- Creating Savings Account ---")
savings1 = SavingsAccount("Charlie", 2000, 0.02)
savings1.deposit(100)
savings1.apply_interest()
print(savings1)
