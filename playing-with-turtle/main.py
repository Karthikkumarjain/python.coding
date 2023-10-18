from turtle import Turtle,Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.color("red")

colours = ["red","green","blue","yellow","purple","orange"]
directios = [0,90,180,270]
timmy.pensize(15)
timmy.speed("fastest")


def random_colour():
    """Returns a random colour"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_c = (r,g,b)
    return random_c


for _ in range(100):
    timmy.color(random_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(directios))

screen.exitonclick()