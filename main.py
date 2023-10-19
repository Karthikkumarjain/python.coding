class Animal:
    def __init__(self):
        self.number_of_legs=4

    def big_animal_breath(self):
        print("big animal breathes")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def big_animal_breath(self):
        super().big_animal_breath()
        print("fish breathes")

nemo =Fish()

nemo.big_animal_breath()

def reverse_A_String(string):
    str= string[::-1]
    print(str)
    return str

reverse_A_String("hello")

def reverse_a_tuple(tuple):
    return tuple[::-1]

print(reverse_a_tuple((1,2,3,4,5)))
