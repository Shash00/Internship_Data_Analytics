class Account:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance

    def deposit(self,deposit_amount):
        self.balance += deposit_amount

    def withdraw(self,withdraw_amount):
        self.balance -= withdraw_amount

    def showinfo(self):
        print(f"Account number: {self.accno}\nName:{self.name} \nBalance:{self.balance}")


name = Account(1001, 'Shashank', 1000)

name.deposit(5000)
name.withdraw(1500)
name.showinfo()


nam2 = Account(1002, 'Mallya', 200)
nam2.deposit(50)
nam2.withdraw(350)
nam2.showinfo()


    