from bank_accounts import *

Atta = bank_account(1000, "Atta")
Amna = bank_account(2000, "Amna")

Atta.getBalance()
Amna.getBalance()

# Atta.deposit(100)
Amna.deposit(500)

Atta.withdraw(1200)
Atta.withdraw(10)

Atta.transfer(5000, Amna)

Sohaib = interestRewardAccount(1000, "Sohaib")

Sohaib.deposit(500)

Sohaib.getBalance()
Sohaib.transfer(100, Atta)

Rubina = savingsAcocunt(2000, "Rubina")
Rubina.getBalance()
Rubina.deposit(500)
Rubina.getBalance()
Rubina.transfer(1000, Atta)
