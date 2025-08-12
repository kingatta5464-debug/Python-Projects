import random


# Function to simulate rolling a 6-sided die
def roll():
    return random.randint(1, 6)


# Ask how many players will play the game
while True:
    no_of_players = input("Enter the number of players (2-4): ")
    if no_of_players.isdigit():
        no_of_players = int(no_of_players)
        if no_of_players < 2 or no_of_players > 4:
            print("Invalid input! Please choose between 2 to 4 players.")
            continue
        else:
            break
    else:
        print("Invalid input! Try again with a number.")

# Initialize each player's total score to 0
players_scores = [0 for _ in range(no_of_players)]
max_score = 50  # Target score to win the game

# Main game loop
while max(players_scores) < max_score:

    # Loop through each player in every round
    for player_index in range(no_of_players):
        current_score = 0
        print(f"\nPlayer {player_index + 1}'s turn has started!")
        print(f"Your current total score is: {players_scores[player_index]}")

        # Player keeps rolling until they stop or roll a 1
        while True:
            should_roll = input("Would you like to roll? (y to roll): ").lower()
            if should_roll != "y":
                break

            roll_value = roll()

            if roll_value == 1:
                print("Oh no! You rolled a 1. Turn over, no points earned.")
                current_score = 0
                break
            else:
                current_score += roll_value
                print(
                    f"You rolled a {roll_value}. Current round score: {current_score}"
                )

        # Add current round score to player's total score
        players_scores[player_index] += current_score
        print(
            f"Total score for Player {player_index + 1}: {players_scores[player_index]}"
        )

# Game over, determine the winner
highest_score = max(players_scores)
winning_index = players_scores.index(highest_score)
print(f"\nPlayer {winning_index + 1} wins the game with a score of {highest_score}!")


# import random


# def roll():
#     roll = random.randint(1, 6)
#     return roll


# while True:
#     no_of_players = input("Enter the number of players (2-4) : ")
#     if no_of_players.isdigit():
#         no_of_players = int(no_of_players)
#         if no_of_players > 4 or no_of_players < 2:
#             print("Invalid Input! Select from 2 - 4")
#             continue
#         else:
#             break
#     else:
#         print("Invalid Input! Try Again!")

# players_scores = [0 for _ in range(no_of_players)]

# max_scores = 50

# while max(players_scores) < max_scores:

#     for players_index in range(len(players_scores)):
#         current_scores = 0
#         print(f"\nPlayer number {players_index+1} turn has just started!")
#         print(f"\nYour total score is : {current_scores}")

#         while True:
#             should_roll = input("\nWould You like to roll? (y) :").lower()
#             if should_roll != "y":
#                 break
#             else:
#                 sc = roll()

#                 if sc == 1:
#                     print("\nYou rolled a 1! Turn Done!")
#                     current_scores = 0
#                     break
#                 else:
#                     current_scores += sc
#                     print(f"\nYou rolled a {sc}")
#             print("Your score is:", current_scores)

#         players_scores[players_index] += current_scores
#         print(f"\nYour total scores are : {players_scores[players_index]}")

# max_score = max(players_scores)
# winning_indx = players_scores.index(max_score)
# print(f"\nPlayer number {winning_indx+1} is the winner with a score of {max_score}.")
