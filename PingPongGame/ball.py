from turtle import Turtle
X = 10
Y = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, 0)

    def move(self, x):
        self.seth(x)
        self.forward(20)


    def reset(self):
        self.setpos(0, 0)