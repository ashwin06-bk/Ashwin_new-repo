class bank:
    def __init__(self,name,ac_no,balance):
        self.name=name
        self.ac_no=ac_no
        self.balance=balance
        self.wamount = 0
        self.Damount = 0
    
    def withdraw(self,Wamount):
        if 0< Wamount <= self.balance:
            self.balance -= Wamount
            self.wamount=Wamount
        else:
            print("please entre a valid amount")

    def deposite(self,Damount):
        
        if Damount >=0:
            self.balance += Damount
            self.Damount=Damount
        else:
            print("please entre a amount greater than 0")

    def display(self):
        print("account holder name:",self.name)
        print("account number:",self.ac_no)
        print("account balance:",self.balance)
        print("withdrawl amount:",self.wamount)
        # print("account balance after withdrawl:",self.wamount)
        print("deposite amount:",self.Damount)
        # print("account balance after deposite:",self.current)

b=bank("ashwin",125658,50000)
b.withdraw(5000)
b.deposite(10000)
b.display()