from turtle import Turtle
DISTANCE = 20


class Design:
    def __init__(self):
        super().__init__()

    def game_env(self):
        mid_line = Turtle()
        mid_line.hideturtle()
        mid_line.color('white')
        mid_line.penup()
        mid_line.goto(0, 360)
        mid_line.right(90)
        for _ in range(34):
            mid_line.pendown()
            mid_line.forward(DISTANCE)
            mid_line.penup()
            mid_line.forward(DISTANCE)

        bound_left = Turtle()
        bound_left = Turtle()
        bound_left.hideturtle()
        bound_left.color('white')
        bound_left.penup()
        bound_left.goto(-360, 360)
        bound_left.right(90)
        for _ in range(60):
            bound_left.pendown()
            bound_left.forward(DISTANCE)

        bound_right = Turtle()
        bound_right = Turtle()
        bound_right.hideturtle()
        bound_right.color('white')
        bound_right.penup()
        bound_right.goto(360, 360)
        bound_right.right(90)
        for _ in range(60):
            bound_right.pendown()
            bound_right.forward(DISTANCE)







