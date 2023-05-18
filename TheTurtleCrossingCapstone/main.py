from turtle import Screen
import time
from scoreboard import Scoreboard
from car_manager import Car
from player import Player
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing Capstone Game")
screen.tracer(0)

player = Player()
car_list = []
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go, "Up")
i = 300
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    new_car = Car(i)
    car_list.append(new_car)
    i += random.randint(7, 30)
    for car in car_list:
        car.move()
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_on = False
        if player.ycor() > 290:
            player.reset()
            scoreboard.traking_score()
            car.next_level()











screen.exitonclick()
