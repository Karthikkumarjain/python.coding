alphabet = ['a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def encrypt(secret_manipultaion, user_shift):
    end_string = ""
    for char in secret_manipultaion:
        if char in alphabet:
            index_found = alphabet.index(char)
            shift_index = index_found + user_shift
            end_string += alphabet[shift_index]
        else:
            end_string+=char
    print(end_string)


def decrypt(secret_manipultaion, user_shift):
    end_string = ""
    for char in secret_manipultaion:
        if char in alphabet:
            index_found = alphabet.index(char)
            shift_index = index_found - user_shift
            end_string += alphabet[shift_index]
        else:
            end_string+=char
    print(end_string)


restart = False
while not restart:
    user_input = input("Do you want to encode or decode?\n")
    secret_manipultaion = input("Enter your message\n").lower()
    user_shift = int(input("How many shifts?"))

    if user_input == "encode":
        encrypt(secret_manipultaion, user_shift)
    elif user_input == "decode":
        decrypt(secret_manipultaion, user_shift)

    should_end = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if should_end == "no":
        restart = True
