from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from table import Table
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
r_scoreboard = Scoreboard(100, 230)
l_scoreboard = Scoreboard(-100, 230)
center = Table()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
x = 45
t = 0.1
while game_on:
    screen.update()
    time.sleep(t)
    ball.move(x)

    if ball.ycor() > 290 or ball.ycor() < -290:
        x = x - x * 2
        t *= 0.9

    elif (ball.xcor() < -330 and ball.distance(l_paddle) < 50) or (ball.xcor() > 330 and ball.distance(r_paddle) < 50):
        x = x + x * 2
        t *= 0.9

    elif ball.xcor() < -390:
        print("Left Gamer Lose")
        r_scoreboard.traking_score()
        ball.reset()
        x = x + x * 2
        t = 0.1

    elif ball.xcor() > 390:
        print("Right Gamer Lose")
        l_scoreboard.traking_score()
        ball.reset()
        x = x + x * 2
        t = 0.1


screen.exitonclick()
