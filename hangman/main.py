import random
from list_of_words import word_list


chosen_word = random.choice(word_list)
word_len =len(chosen_word)

print(f"The chosen word is {chosen_word}")

from pictures import logo

print(logo)

end_game = False

lives = 6

display = []
for _ in range(word_len):
    display.append("_")


while not end_game:
    guess = input("User's iput- Enter ur guess")
    for position in range(word_len):
        addvariableselector=chosen_word[position]
        if addvariableselector==guess:
            display[position]=addvariableselector
    print(display)
    if guess not in chosen_word:
        lives-=1
        from pictures import stages
        print(stages[lives])
        if lives==0:
            print("u lose")
            end_game=True
    if "_" not in display:
        print("You win")
        end_game=True
    print(f"{' '.join(display)}")

