from turtle import Turtle

ALIGMENT = 'center'
FONT= ('Courier', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.hideturtle()
        self.penup()
        self.setpos(self.x, self.y)
        self.color("white")
        self.score = 0
        self.update()

    def update(self):
        self.write(f'{self.score}', True, ALIGMENT, font=FONT)

    def traking_score(self):
        self.clear()
        self.score += 1
        self.setpos(self.x, self.y)
        self.update()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f'GAME OVER', True, ALIGMENT, font=FONT)
