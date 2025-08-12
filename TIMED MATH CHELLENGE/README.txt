Math Quiz Game

Description:
------------
This is a simple Python math quiz program that:
  - Generates random arithmetic problems using addition, subtraction, and multiplication.
  - Tracks the total time taken to solve all problems.
  - Counts how many wrong attempts were made before getting each answer right.

Features:
---------
1. 10 random problems are generated (by default).
2. Operands are between 3 and 12.
3. Randomly picks from +, -, * operators.
4. Measures how fast the user solves all problems.
5. Tracks incorrect attempts.

How It Works:
-------------
- The program uses Python's 'random' module to generate numbers and operators.
- It evaluates the correct answer internally using 'eval()'.
- The user must enter the correct answer before moving to the next problem.
- At the end, the program shows:
    1. Total time taken.
    2. Number of wrong attempts.

Requirements:
-------------
- Python 3.x

Run Instructions:
-----------------
1. Save this file (e.g., math_quiz.py).
2. Open a terminal or IDE.
3. Run:
      python math_quiz.py

Sample Output:
--------------
Press Enter To Start!

----------------------
Problem 1 : 7 + 5 = 12
Problem 2 : 9 * 3 = 27
Problem 3 : 8 - 4 = 4
...
----------------------
Nice work! You finished in 15.32 seconds!
2 times you gave wrong answer.

Author:
-------
Atta Ul Mustafa
