import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(answer, guess, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print("You got the right answer")


def set_difficulty():
    level_of_game = input("Choose the level of game you wnt to play : easy or hard?").lower()
    if level_of_game == "easy":
        return EASY_LEVEL_TURNS
    elif level_of_game == "hard":
        return HARD_LEVEL_TURNS


def start_game():
    print(logo)
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0

    print(f"the value is {answer}")
    while guess != answer:
        print(f"You have this many attempts left{turns}")
        guess = int(input("Enter your guess"))
        turns = check_answer(answer, guess, turns)
        if turns == 0:
            print("Your turns are over,you Lose!!")
            return

start_game()