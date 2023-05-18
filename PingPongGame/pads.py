from turtle import Turtle



class Pads:
    def __init__(self):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(5, 1)
        self.paddle.setpos(350, 0)

