import turtle as t 
from turtle import Screen
import random

timmy = t.Turtle()  #initialization of the turtle class object
t.colormode(255)
timmy.shape("arrow")

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col   #returning a tuple



"""
colors = ["dark blue", "pale violet red", "rosy brown", "deep sky blue",  "forest green", "steel blue", "firebrick","olive drab", "indigo",  "sienna", "orange red" ]
"""
step =  30
directions = [0, 90, 180, 270]
timmy.pensize(10)
for _ in range(300):
    timmy.color(random_color())
    timmy.fd(step)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
