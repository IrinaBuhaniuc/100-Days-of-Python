from turtle import Turtle


class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.pensize(5)
        self.make_linie()

    def make_linie(self):
        self.setpos(0, 300)
        self.seth(270)
        for n in range(-290, 0):
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()


