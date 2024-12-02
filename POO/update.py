# Exercise 7: Update Methods

# Add a method to the BankAccount class called update_holder that allows changing the account holder's name.

# Create an instance of the class, change the account holder's name, and display the balance and the new holder.


class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, value):
        self.balance += value if value > 0 else 0

    def withdraw(self, value):
        self.balance -= value if self.balance >= value else 0

    def check_balance(self):
        print(f"{self.holder} You're balance is: ${self.balance}")

    def update_holder(self, new_holder):
        if self.holder:
            self.holder = new_holder
            print("Holder updated successfully")

client1 = BankAccount('Matt', 2000)

client1.deposit(500)
client1.check_balance()

client1.withdraw(1500)
client1.check_balance()
client1.update_holder('Bryan')
client1.check_balance()
