# SavingAccount class with id, customer, balance
# Methods: deposit, withdraw, get_balance
# Handle validation and raise errors when validation fails

class SavingAccount:
    def __init__(self, account_id, customer_name, initial_balance=0):
        self.account_id = account_id
        self.customer_name = customer_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


