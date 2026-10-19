class Bank_Account:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print("Account Holder:",self.account_holder)
        print("Account Number:",self.account_number)
        print("Balence:",self.balance)

    def deposite(self,amount):
        if amount>=0:
            print("Deposite Successfuly")

        else:
            print("Invalid Amount")

    def check_balance(self):
        return self.balance + self.deposite

    


account1 = Bank_Account("Ashwin",101,5000)
account2 = Bank_Account("Rohan",102,10000)

account1.deposite(200)
print("-----Account 1-----")
account1.display_details()
account1.check_balance()


print("-----Account 2-----")
account2.display_details()





