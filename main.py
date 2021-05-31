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
from food import Food
from score_board import ScoreBoard
import time

# Main screen setup
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The Snake Game")
my_screen.tracer(0)  # turn tracer off / animation off

snake = Snake()
food = Food()
sb = ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

snake.is_alive = False
while snake.is_alive:
    my_screen.update()  # turn tracer on / update animation after progress happens
    # we use the timer to delay the animation refresh otherwise we cannot see it happen
    time.sleep(.1)  # slightly delay by .1 seconds after every animation update

    snake.move()

    #  detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.update()

my_screen.exitonclick()
