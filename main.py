from turtle import Screen
from design import Design
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title('PONG MASTERS')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
design = Design()
design.game_env()


screen.listen()
screen.onkey(fun=r_paddle.upward, key='Up')
screen.onkey(fun=r_paddle.downward, key='Down')
screen.onkey(fun=l_paddle.upward, key='w')
screen.onkey(fun=l_paddle.downward, key='s')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(l_paddle) <= 25 and ball.xcor() <= -320:
        ball.detect_paddle()

    elif ball.distance(r_paddle) <= 25 and ball.xcor() >= 320:
        ball.detect_paddle()

    if ball.xcor() < -360:
        scoreboard.clear()
        ball.reset_position()
        scoreboard.increase_score_2()

    elif ball.xcor() > 360:
        scoreboard.clear()
        ball.reset_position()
        scoreboard.increase_score_1()


screen.exitonclick()