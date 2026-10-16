class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def display_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)

account.deposit(1000)
account.display_balance()