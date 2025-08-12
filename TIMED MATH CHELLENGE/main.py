import random
import time

operators = ["+", "-", "*"]
total_problems = 10

min_operand = 3
max_operand = 12


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    op = random.choice(operators)
    experssion = str(left) + " " + op + " " + str(right)
    answer = eval(experssion)
    return experssion, answer


wrong = 0

input("Press Enter To Start!\n")
print("----------------------")

start_time = time.time()
for i in range(total_problems):
    exp, ans = generate_problem()

    while True:
        answer = input(f"Problem {i+1} : {exp} = ")
        if answer == str(ans):
            break
        wrong += 1
end_time = time.time()

total_time = end_time - start_time

print("----------------------")
print(f"Nice work! You finished in {total_time:.2f}seconds!")
print(f"{wrong} times you gave wrong answer.")
