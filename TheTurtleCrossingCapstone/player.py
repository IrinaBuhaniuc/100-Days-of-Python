from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.setpos(0, -280)
        self.color("Black")

    def go(self):
        self.forward(10)
        if self.ycor() > 280:
            self.forward(0)

    def reset(self):
        self.setpos(0, -280)
