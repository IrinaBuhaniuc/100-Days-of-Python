from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    score: int

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.h_score = data.read()
        self.high_score = int(self.h_score)
        self.setpos(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.setpos(0, 270)
        self.write(f'Score: {self.score}  High Score: {self.high_score}', True, ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
#    def game_over(self):
#        self.setpos(0, 0)
#        self.write('GAME OVER', True, ALIGNMENT, font=FONT)

    def tracking_score(self):
        self.score += 1
        self.setpos(0, 270)
        self.update()
