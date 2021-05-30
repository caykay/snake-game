# STEPS
# 1. Create a snake body  ✅
# 2. Move the snake  ✅
# 3. Create snake food
# 4. Detect collision w/ food
# 5. Create a scoreboard
# 6. Detect collision with a wall
# 7. Detect collision with tail

from turtle import Screen
from snake import Snake
import time

# Main screen setup
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The Snake Game")
my_screen.tracer(0)  # turn tracer off / animation off

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

while snake.is_alive:
    my_screen.update()  # turn tracer on / update animation after progress happens
    # we use the timer to delay the animation refresh otherwise we cannot see it happen
    time.sleep(.1)  # slightly delay by .1 seconds after every animation update

    snake.move()

my_screen.exitonclick()
