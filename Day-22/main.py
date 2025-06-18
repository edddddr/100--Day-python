from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong ⚾⚾⚾")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()

screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with all
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()
    
    #  Detect collision wiht r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
       ball.bounce_x()

    # Detect R paddle misses
    if  ball.xcor() > 380:
        ball.reset_pos()

    if  ball.xcor() < - 380:
        ball.reset_pos()




screen.exitonclick()