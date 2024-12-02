# Exercise 3: Basic Operations

# Create a class called BankAccount with the attributes holder and balance.

# Add methods to deposit and withdraw money from the account, and a method to check_balance.

# Create an instance of the class and perform some deposit and withdrawal operations, showing the balance after each operation.

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, value):
        self.balance += value if value > 0 else 0

    def withdraw(self, value):
        self.balance -= value if self.balance >= value else 0

    def check_balance(self):
        print(f"You're balance is: ${self.balance}")

client1 = BankAccount('Matt', 2000)

client1.deposit(500)
client1.check_balance()

client1.withdraw(1500)
client1.check_balance()