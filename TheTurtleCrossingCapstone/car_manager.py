from turtle import Turtle
import random

COLORS = ["red", "purple", "orange", "blue", "yellow", "green"]

class Car(Turtle):
    def __init__(self, x):
        super().__init__()
        self.create_car(x)

    def create_car(self, x):
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.setpos(x, random.randint(-260, 260))
        self.start = 5

    def move(self):
        self.seth(180)
        self.forward(self.start)

    def next_level(self):
        self.start += 10



