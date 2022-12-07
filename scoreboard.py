from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-160, 200)
        self.write(self.score_1, font=('Courier', 80, 'normal'))

        self.goto(100, 200)
        self.write(self.score_2, font=('Courier', 80, 'normal'))

    def increase_score_1(self):
        self.score_1 += 1
        self.update_scoreboard()

    def increase_score_2(self):
        self.score_2 += 1
        self.update_scoreboard()





