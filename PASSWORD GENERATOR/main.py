import string
import random


def generate_password(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    pwd = ""
    has_digits = False
    has_special = False
    meet_criteria = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_digits = True
        if new_char in special:
            has_special = True

        meet_criteria = True

        if numbers:
            meet_criteria = has_digits
        if special_char:
            meet_criteria = meet_criteria and has_special
    return pwd


password = generate_password(10)
print(password)
password = generate_password(10, False)
print(password)
password = generate_password(10, False, False)
print(password)
