from datetime import datetime


class bankaccount:
    def __init__(self, accountnumber, balance=0):
        self.accountnumber = accountnumber
        self.balance = balance

    def _transaction(self, transaction_type, amount):
        with open("transactions.txt", "a") as file:
            file.write(
                f"Time: {datetime.now()}  {transaction_type} of Amount {amount}$.\n"
            )

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._transaction("Deposit", amount)
            print(f"Deposited Amount : {amount}$")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            self._transaction("Withdrew", amount)
            print(f"withdrew Amount : {amount}$")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        print(f"Balance : {self.balance}$")


a1 = bankaccount(123690, 4000)
a1.get_balance()
a1.deposit(2000)
a1.withdraw(180)
a1.withdraw(1100)
a1.withdraw(11000)
