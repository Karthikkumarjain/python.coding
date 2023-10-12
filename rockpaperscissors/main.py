import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
computer_choise = random.randint(0, 2)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input == 0:
    print(rock)

    print(f"Computer chose:{computer_choise}")
    print(game[computer_choise])
elif user_input == 1:
    print(paper)

    print(f"Computer chose:{computer_choise}")
    print(game[computer_choise])
elif user_input == 2:
    print(scissors)

    print(f"Computer chose:{computer_choise}")
    print(game[computer_choise])
else:
    print("invalid choice")

if user_input == 0 and computer_choise == 2:
    print("You win")
elif user_input == 2 and computer_choise == 1:
    print("You win")
elif user_input == 1 and computer_choise == 0:
    print("You lose")
elif user_input == 2 and computer_choise == 0:
    print("You lose")
elif user_input == 1 and computer_choise == 2:
    print("You lose")
elif user_input == 0 and computer_choise == 1:
    print("You win")
elif user_input == computer_choise:
    print("Draw")
else:
    print("invalid choice")
