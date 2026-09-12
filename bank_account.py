class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.amount=amount
        self.balance -= amount
        print("rs", amount,"is debited")


    def credit(self, amount):
            self.amount=amount
            self.balance += amount
            print("rs", amount,"is credit")

    def check_balance(self):
         return self.balance

acc1 = Account(10000, "24100btmlccgc17583")
acc1.credit(2000)
print(acc1.check_balance())      
acc1.debit(1000)
print(acc1.check_balance())
