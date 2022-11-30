from turtle import Screen
from pong import Pong
from ball import Ball
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

ball = Ball()
r_paddle = Pong((350, 0))
l_paddle = Pong((-350, 0))
score = Score()
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.spd)
    ball.move()
    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        # game_on = False
    if ball.xcor() > 410:
        ball.refresh()
        score.increase_score()
    if ball.xcor() < -410:
        ball.refresh()
        score.increase_score2()

screen.exitonclick()
