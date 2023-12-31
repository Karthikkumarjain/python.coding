import turtle as t
from turtle import Screen
import random

t = t.Turtle()
screen = Screen()
t.speed("fastest")
screen.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r, g, b)
    return random_c

def create_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(random_colour())
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)

# for _ in range(100):
#     t.color(random_colour())
#     t.circle(100)
#     t.setheading(t.heading()+10)
#     print(t.heading())

create_spirograph(5)

screen.exitonclick()
