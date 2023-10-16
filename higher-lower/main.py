# Load the images
# Print the welcome message along with what it is comparing
# Ask the user to choose which one is higher or lower
# Compare the values  of the user and the file for specific key
# Print if success or failure
# If success ,
#   play again and increase the score
# Compare the last B with nxt random
# If failure, exit the game and display the score

from game_data import data
import random
from art import logo, vs

print(logo)


def check_answer(choice_a, choice_b, guess):
    follower_count_a = choice_a["follower_count"]
    follower_count_b = choice_b["follower_count"]
    if follower_count_a > follower_count_b:
        return guess == "a"
    else:
        return guess == "b"


score = 0
play_game = True

choice_b = random.choice(data)
while play_game:

    choice_a = choice_b

    if choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"Choice A is {choice_a["name"]}")
    print(vs)
    print(f"Choice B is {choice_b["name"]}")

    guess = input("Guess which has highest follower from your end").lower()
    correct_ans = check_answer(choice_a, choice_b, guess)
    print(correct_ans)

    if correct_ans == True:
        score += 1
    else:
        play_game = False
        print(f"Final score is {score}")
