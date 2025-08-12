import random

easy_words = ["apple", "train", "tiger", "money", "egypt"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("WELCOME TO PASSWORD GUESSING GAME\n")
print("Choose a difficulty level : \n1. Easy\n2. Medium\n3. Hard")

choice = int(input("Enter the choice : "))

if choice == 1:
    secret = random.choice(easy_words)
elif choice == 2:
    secret = random.choice(medium_words)
elif choice == 3:
    secret = random.choice(hard_words)
else:
    print("Invalid Choice. Defaulting to easy level.")
    secret = random.choice(easy_words)


length = len(secret)
attempts = 0
print(f"\nLength of password is {length}")
print("\nGuess the password.")

while True:
    guess = input("Enter Your Guess : ")
    attempts += 1
    if guess == secret:
        print(f"Congratulations! You Guessed it in {attempts} attempts.")
        break
    else:
        hint = ""
        for i in range(length):
            if i < len(guess) and guess[i] == secret[i]:
                hint = hint + secret[i]
            else:
                hint = hint + "-"
        print(f"Your hint is as : {hint}")
