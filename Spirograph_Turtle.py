import turtle as t
from turtle import *
import random


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col 

timmy = t.Turtle()
t.colormode(255)
timmy.speed('fastest')

for i in range(20):
    timmy.color(random_color())
    timmy.circle(80)
    timmy.left(20)

screen = Screen()
screen.exitonclick()
