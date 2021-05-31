from turtle import Turtle

ALIGNMENT = "center"
FONT_1 = ("Comic sans MS", 10, "normal")
FONT_2 = ("Comic sans MS", 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.sety(280)
        self.score = 0
        self.display()

    def update(self):
        """Updates the score board"""
        self.clear()  # delete drawings on screen but doesn't move
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)  # the center
        self.write(arg=f"GAME OVER.\n  SCORE: {self.score}", align=ALIGNMENT, font=FONT_2)

    def display(self):
        """Display the writing on the screen"""
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT_1)
