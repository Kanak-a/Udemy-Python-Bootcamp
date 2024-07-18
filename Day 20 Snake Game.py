from turtle import Screen, Turtle

#a new screen
screen = Screen()  #object
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Snake Game")
#animation control
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

#step 1 : Create the snake body
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.goto(position)
    segments.append(new_segment)

#updating after all the segments are created
screen.update()

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)














screen.exitonclick()