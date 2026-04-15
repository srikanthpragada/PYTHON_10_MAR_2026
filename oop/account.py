class Account:
    minbal = 10000

    def __init__(self, acno, customer, balance=0):
        self.acno = acno
        self.customer = customer
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - Account.minbal >= amount:
            self.__balance -= amount
        else:
            print("Sorry! Insufficient Balance!")

    def getbalance(self):
        return self.__balance


a = Account(1, "Smith", 15000)
a.deposit(10000)
print(a.getbalance())
a.withdraw(20000)

print(a.__balance)
