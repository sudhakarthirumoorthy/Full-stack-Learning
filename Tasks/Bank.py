
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_account(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)
        print()

    def deposit(self, amount):
        self.balance = self.balance + amount


account1 = BankAccount("Sudhakar", 5000)
account2 = BankAccount("Rahul", 3000)

account1.deposit(1000)

account1.display_account()
account2.display_account()
