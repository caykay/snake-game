# STEPS
# 1. Create a snake body
# 2. Move the snake
# 3. Create snake food
# 4. Detect collision w/ food
# 5. Create a scoreboard
# 6. Detect collision with a wall
# 7. Detect collision with tail

from turtle import Turtle, Screen

# Main screen setup
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The Snake Game")
# initial snake length and position
turtles = []
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
for pos in starting_pos:
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.setpos(pos)
    turtles.append(new_turtle)

my_screen.exitonclick()
