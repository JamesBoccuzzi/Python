class account:
    def __init__(self,balance):
        self.balance = balance
        
    def display(self):
        print(self.balance)
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        
    def withdraw(self,amount):
        self.balance = self.balance - amount
        

a = account(0)
a.display()

a.deposit(4)
a.display()

a.withdraw(2)
a.display()