class balanceException(Exception):
    pass


class bank_account:
    def __init__(self, initialamount, accountname):
        self.balance = initialamount
        self.name = accountname
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n${amount:.2f} deposited to {self.name}'s Account.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise balanceException(
                f"\nSorry, account '{self.name}' has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdrawl of ${amount:.2f} Completed.")
            self.getBalance()
        except balanceException as error:
            print(f"\nWithdraw Intterrupted! {error}")

    def transfer(self, amount, account):
        try:
            print("\n\nBeginning Transfer....")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer Completed.")

        except balanceException as error:
            print(f"\n\nTransfer Interrupted! {error}")


class interestRewardAccount(bank_account):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Completed.")


class savingsAcocunt(interestRewardAccount):
    def __init__(self, initialamount, accountname):
        super().__init__(initialamount, accountname)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Completed")
            self.getBalance()
        except balanceException as e:
            print(f"Withdraw Interrupted. {e }")
