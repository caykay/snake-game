from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]  # starting positions
MOVE_DISTANCE = 20  # distance is 20 because that is the size of each box
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:  # 🐍
    """Creation and motion of the snake's body is managed by this class's instance """
    def __init__(self):
        self.fragments = []
        self.is_alive = True
        self.create_body()
        self.head = self.fragments[0]

    def create_body(self):
        """Create the initial snake body. initial size = 3 fragments."""
        for pos in STARTING_POS:
            self.add_fragment(pos)

    def add_fragment(self, position):
        new_frag = Turtle("square")
        new_frag.color("white")
        new_frag.penup()
        new_frag.setpos(position)
        self.fragments.append(new_frag)

    def extend(self):
        """Increases the snake's fragments by one"""
        last_frag_pos = self.fragments[-1].pos()
        # the new fragment will take the position of the very last fragment
        # so on the very slight next move the positions will be adjusted
        # such that the snake appears at an expected length
        self.add_fragment(last_frag_pos)

    def move(self):
        """The moving mechanics are such that the last fragment follows the position of that next to it
        to the first fragment. This way it is easier to keep track of the positioning increment."""
        for frag_num in range(self.length() - 1, 0, -1):
            new_pos = self.fragments[frag_num - 1].pos()
            self.fragments[frag_num].goto(new_pos)
        self.fragments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Go up.
        Only go up when not pointing down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Go south.
        Only turn south when not facing up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn left.
        Cannot turn left if facing right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn right.
        Only turn right when not facing left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def length(self):
        """Current number of fragments."""
        return len(self.fragments)
