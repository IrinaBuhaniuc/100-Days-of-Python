from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
XCORD = 0


class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_snake()
        self.head = self.my_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setpos(position)
        self.my_snake.append(snake)

    def extend(self):
        self.add_snake(self.my_snake[-1].position())

    def move(self):
        for n in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[n - 1].xcor()
            new_y = self.my_snake[n - 1].ycor()
            self.my_snake[n].setpos(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def reset(self):
        for snake in self.my_snake:
            snake.setpos(1000, 1000)
        self.my_snake.clear()
        self.create_snake()
        self.head = self.my_snake[0]