# STEPS
# 1. Create a snake body
# 2. Move the snake
# 3. Create snake food
# 4. Detect collision w/ food
# 5. Create a scoreboard
# 6. Detect collision with a wall
# 7. Detect collision with tail

from turtle import Turtle, Screen
import time

# Main screen setup
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The Snake Game")
my_screen.tracer(0)  # turn tracer off / animation off

# initial snake length and position
portions = []
starting_pos = [(0, 0), (-20, 0), (-40, 0)]

for pos in starting_pos:
    new_portion = Turtle("square")
    new_portion.color("white")
    new_portion.penup()
    new_portion.setpos(pos)
    portions.append(new_portion)

play_game = True
while play_game:
    my_screen.update()  # turn tracer on / update animation after progress happens
    time.sleep(.1)  # slightly delay by .1 seconds after every animation update
    # if the sleep is not used then the duration window of screen.update() will be
    # a fraction of a second not visible by the eye
    for por_num in range(len(portions) - 1, 0, -1):
        new_pos = portions[por_num - 1].pos()
        portions[por_num].goto(new_pos)
    portions[0].forward(20)  # distance is 20 because that is the size of each box

my_screen.exitonclick()
