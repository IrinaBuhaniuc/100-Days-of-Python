from turtle import Turtle, Screen, colormode
from random import randint, randrange


annie = Turtle()
annie.shape("arrow")
annie.color("purple")
#annie.left(180)
#annie.forward(100)
#for _ in range(3):
#    annie.right(90)
#    annie.penup()
#    annie.forward(50)
#    annie.pendown()
#    annie.forward(50)
#annie.penup()
#annie.backward(200)
#for _ in range(50):
#    annie.forward(5)
#    annie.penup()
#    annie.forward(5)
#    annie.pendown()
annie.speed(0)
#i= 3
colormode(255)
#for n in range(8):
#    for _ in range(i):
#        annie.forward(50)
#        annie.right(360/i)
#    i+= 1
#    annie.color(randint(0, 255), randint(0, 255), randint(0, 255))
#n=10
#annie.width(10)

#for _ in range(1, 50):
    #annie.goto(random.randint(-10, 0), random.randint(0, 10))
    #annie.seth(randrange(0, 360, 90))
    #annie.forward(randint(0, 30))
    #annie.color(randint(0, 255), randint(0, 255), randint(0, 255))
    #annie.width(n)
    #n+1
n= 0
annie.heading()


def draw_spirograph(set_of_gap):
    for n in range(int(360/ set_of_gap)):
        annie.circle(100)
        annie.setheading(annie.heading()+set_of_gap)
        annie.color(randint(0, 255), randint(0, 255), randint(0, 255))


draw_spirograph(5)


screen = Screen()
screen.exitonclick()


