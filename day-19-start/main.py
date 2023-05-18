import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Whitch turtle will winn the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []
h = -80

for colour in colours:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=h)
    h += 30
    turtles_list.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You've won. The winner is {winner}")
            else:
                print(f"You've lose. The winner is {winner}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)







screen.exitonclick()