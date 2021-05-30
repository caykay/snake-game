from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]  # starting positions
MOVE_DISTANCE = 20  # distance is 20 because that is the size of each box


class Snake:
    """Creation and motion of the snake's body is managed by this class's instance """
    def __init__(self):
        self.fragments = []
        self.is_alive = True
        self.create_body()

    def create_body(self):
        for pos in STARTING_POS:
            new_frag = Turtle("square")
            new_frag.color("white")
            new_frag.penup()
            new_frag.setpos(pos)
            self.fragments.append(new_frag)

    def move(self):
        for frag_num in range(self.length() - 1, 0, -1):
            new_pos = self.fragments[frag_num - 1].pos()
            self.fragments[frag_num].goto(new_pos)
        self.fragments[0].forward(MOVE_DISTANCE)

    def length(self):
        return len(self.fragments)
