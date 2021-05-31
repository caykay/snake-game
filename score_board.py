from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.sety(280)
        self.score = 0
        self.display()

    def update(self):
        """Updates the score board"""
        self.clear()  # delete drawings on screen but doesn't move
        self.score += 1
        self.display()

    def display(self):
        """Display the writing on the screen"""
        self.write(arg=f"Score: {self.score}", align="center", font=("Comic sans MS", 10, "normal"))
