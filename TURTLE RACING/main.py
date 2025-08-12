import turtle
import random


HEIGHT = 500
WIDTH = 1000

COLORS = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "black",
    "cyan",
    "pink",
    "brown",
    "orange",
]


def get_no_racers():
    while True:
        racers = input("Enter Number of Turtles : ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try Again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try Again!")


def set_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, colr in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(colr)
        racer.shape("turtle")
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.left(90)
        racer.pendown()

        turtles.append(racer)
    return turtles


def race(colors):
    turtles = create_turtles(colors)

    input("\nPress 'Enter' to start the game!")
    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)

            x, y = racer.pos()

            if y >= (HEIGHT // 2 - 10):
                return colors[turtles.index(racer)]


racers = get_no_racers()
set_screen()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)

print(f"\n🎉 The winner is the turtle with color: {winner.upper()} 🎉")

turtle.done()
