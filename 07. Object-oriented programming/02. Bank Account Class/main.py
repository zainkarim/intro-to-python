# DRILL: BankAccount
# Write a class BankAccount. This class has one
# instance variable "balance" and four methods each
# of which requires only one line of code each:
#   constructor: take as input an amount and
#                initialize "balance"
#   deposit: take as input an amount and increment
#            "balance"
#   withdraw: take as input an amount and decrement
#             "balance"
#   overdrawn: return True if "balance" is less
#              than 0, else return False
# 
# Write a small driver code to test all functions

# BankAccount
class BankAccount:
    # Constructor
    def __init__(self, balance):
        self.balance = balance

    # RETURN current account balance
    def __str__(self):
        return "Current balance: $" + str(self.balance)
    
    # Deposit function
    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    # Withdraw function
    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount

    # Overdrawn function
    def overdrawn(self):
        return self.balance < 0

# Check account balance
account = BankAccount(2000.00)
print(account)

# Deposit
account.deposit(1200)
print(account)

# Withdraw
account.withdraw(3200)
print(account)

# Overdrawn
print(account.overdrawn())