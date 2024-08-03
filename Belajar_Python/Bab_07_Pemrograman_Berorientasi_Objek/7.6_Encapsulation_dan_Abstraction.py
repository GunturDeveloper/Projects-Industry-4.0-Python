# Enkapsulasi dan Abstraksi
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Atribut privat

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())
