from cal_functions import *

print("----SIMPLE CALCULATOR----")
print("----type( history, clear, exit )----")


while True:
    show_menu()
    choice = int(input("Enter your choice (1-4) : \n"))
    if choice == 1:
        user_input = input("Enter expression (e.g., 5+5 or 8 * 3): ")
        calculate(user_input)
    elif choice == 2:
        show_history()
    elif choice == 3:
        clear_history()
    elif choice == 4:
        print("Exiting Calculator. Goodbye Atta bhai 👋")
        break
    else:
        print("Invalid choice. Please enter 1 to 4.")
