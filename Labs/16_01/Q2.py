class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def transaction(self, deposit,withdrawl):
        if withdrawl>self.balance:
            print("Insufficient balance, Withdrawl is not allowed")
        else:
            self.balance=self.balance+deposit
            self.balance=self.balance-withdrawl
            print("Transaction made")
            print("Account number:",self.account_number)
            print("Balance:",self.balance)
    def __del__(self):
        print("BankAccount object is deleted")

acc1=BankAccount(1,1000)
acc1.transaction(500,300)
acc2=BankAccount(2,300)
acc2.transaction(100,800)

del acc1
del acc2