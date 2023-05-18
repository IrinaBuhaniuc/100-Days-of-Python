import turtle
from turtle import Turtle, Screen
import random


colors_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
               (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
               (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),
               (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
               (156, 212, 190), (87, 46, 33), (37, 45, 83)]

annie = Turtle()
turtle.colormode(255)
annie.hideturtle()
annie.penup()


def raw_dot(nr_dots):
    for _ in range(0, nr_dots):
        annie.dot(20, random.choice(colors_list))
        annie.forward(50)


annie.setpos(-250, -200)
pos1 = -250
pos2 = -200
for _ in range(0, 10):
    raw_dot(10)
    pos2 += 50
    annie.setpos(pos1, pos2)

screen = Screen()
screen.exitonclick()