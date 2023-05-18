from turtle import Turtle


class State(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(x, y)
        self.state = state
        self.color("black")
        self.write(self.state)

