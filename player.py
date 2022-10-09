from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.reset()

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def is_at_finish_y(self):
        if self.ycor() > 280:
            return True
        return False

    def reset(self):
        self.goto(0, -FINISH_LINE_Y)