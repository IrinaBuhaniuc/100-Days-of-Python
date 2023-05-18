from turtle import Screen
import time
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing Capstone Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False
    if player.is_at_finish_line():
        player.reset()
        scoreboard.traking_score()
            #car.next_level()



screen.exitonclick()