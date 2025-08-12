def show_history():
    file = open("history.txt", "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No History found!")
    else:
        for line in lines:
            print(line.strip())
    file.close()


def clear_history():
    file = open("history.txt", "w")  # this will delete all content in history file.
    file.close()
    print("\nHistory Cleared.")


def save_to_history(equation, result):
    with open("history.txt", "a") as file:
        file.write(equation + " = " + str(result) + "\n")


def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input! Use Format: number operator number (e.g; 8+12)")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide with zero.")
            return
        result = num1 / num2
    else:
        print("Invalid Operator. Use only +,-,* or /.")
        return

    result = int(result)

    print("Result: ", result)
    save_to_history(user_input, result)


def show_menu():
    print("\n==== Atta's Calculator ====")
    print("1. Calculate")
    print("2. Show History")
    print("3. Clear History")
    print("4. Exit")


# a = "5 + 5"
# b = a.split()
# print(b)
