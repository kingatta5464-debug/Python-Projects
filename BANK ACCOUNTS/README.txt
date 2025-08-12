Bank Account Management System (Python OOP Project)

Description:
This is a simple Python project that demonstrates Object-Oriented Programming (OOP) concepts such as:
- Classes
- Inheritance
- Method Overriding
- Exception Handling
- Encapsulation

The project simulates a banking system where you can:
- Create bank accounts
- Deposit money
- Withdraw money
- Transfer money between accounts
- Apply special account rules like interest rewards and withdrawal fees

Files:
- bank_accounts.py → Contains the main classes:
    1. bank_account
    2. interestRewardAccount (inherits from bank_account)
    3. savingsAcocunt (inherits from interestRewardAccount)
    4. balanceException (custom exception for insufficient funds)

- main.py → Contains example usage of the classes and methods.

Features:
1. **bank_account class**
   - Create an account with a name and initial balance
   - Deposit money
   - Withdraw money with balance check
   - Transfer money between accounts

2. **interestRewardAccount class**
   - Inherits from bank_account
   - Overrides deposit method to add 5% bonus on each deposit

3. **savingsAcocunt class**
   - Inherits from interestRewardAccount
   - Adds a $5 fee on each withdrawal

4. **balanceException**
   - Raises a custom exception when a transaction is not possible due to low balance

How to Run:
1. Make sure Python is installed on your system.
2. Save `bank_accounts.py` and `main.py` in the same folder.
3. Open terminal/command prompt in the folder.
4. Run:
   python main.py

Example Output:
--------------------
Account 'Atta' created.
Balance = $1000.00

Account 'Amna' created.
Balance = $2000.00
...
--------------------

Author:
Atta Ul Mustafa
