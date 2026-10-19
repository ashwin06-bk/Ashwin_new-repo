class BankAccount:

    def _init_(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        print("Current balance:", self.__balance)


# Create an object
account = BankAccount(10000)

account.check_balance()

account.deposit(2000)

account.withdraw(3000)

account.check_balance()