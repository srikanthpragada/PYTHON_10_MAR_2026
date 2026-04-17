class InvalidAmountError(Exception):
     def __str__(self):
         return "Invalid Amount!"


class Account:
    minbal = 10000

    def __init__(self, acno, customer, balance=0):
        self.acno = acno
        self.customer = customer
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError()

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Invalid Amount!')

        if self.__balance - Account.minbal >= amount:
            self.__balance -= amount
        else:
            raise ValueError('Insufficient Balance!')

    def getbalance(self):
        return self.__balance


a = Account(1, "Smith", 15000)
try:
    a.deposit(-10000)
    print(a.getbalance())
except InvalidAmountError as e:
    print(e)

try:
    a.withdraw(20000)
    print('Withdrawl Successful!')
except ValueError as e:
    print(e)

#print(a.__balance)
