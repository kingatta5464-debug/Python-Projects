import random

subjects = [
    "Imran Khan",
    "Nawaz Sharif",
    "Shahid Afridi",
    "A Lahore cat",
    "A group of Monkeys",
    "COAS Asim Munir",
    "Auto rikshaw driver from Karachi",
]

actions = [
    "launches",
    "eats",
    "run",
    "declares war on",
    "cuddles",
    "celebrates",
    "order onion",
    "dances",
]

places_or_things = [
    "at Lahore Fort.",
    "in metro bus.",
    "a plate of samosas.",
    "inside parliament",
    "at Minar-e-Pakistan.",
    "during PSL match.",
    "in Anarkali Bazar.",
    "while having fun.",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING THINGS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you wan t another Headline? (yees/no) :\n").strip().lower()

    if user_input == "no":
        break

print("\nThanks for using Fake Headlines Generator. Have a fun day.")
