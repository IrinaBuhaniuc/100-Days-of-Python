from turtle import Turtle

ALIGMENT = 'center'
FONT= ('Courier', 24, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 0
        self.setpos(-230, 270)
        self.update()


    def update(self):
        self.write(f'Level: {self.level}', True, ALIGMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f'GAME OVER', True, ALIGMENT, font=FONT)

    def traking_score(self):
        self.clear()
        self.level += 1
        self.setpos(-230, 270)
        self.update()



