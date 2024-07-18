from turtle import *
import random

timmy = Turtle()
timmy.shape("turtle")

def draw_timmy(num_sides, steps= 50):
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy.fd(steps)
        timmy.right(angle)

#list of colors 
colors = ["pale violet red", "rosy brown","deep sky blue",  "forest green", "steel blue", "firebrick","olive drab", "salmon", "indian red", "light coral", "rosy brown", "hot pink", "plum"]

for i in range(3, 8):
    timmy.color(random.choice(colors))
    draw_timmy(i)
    

screen = Screen()
screen.exitonclick()
