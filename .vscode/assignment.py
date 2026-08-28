class Bank:
    def __init__(self):
        self.__balance=1000
    def deposit(self):
        self.__balance+=500
    def withdraw(self):
        self.__balance-=200
    def getbalance(self):
        return self.__balance
b=Bank()
b.deposit()
b.withdraw()
print(b.getbalance())
