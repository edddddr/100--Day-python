from turtle import Turtle, Screen 
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong ⚾⚾⚾")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((350, 0))


screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'Up')
screen.onkey(l_paddle.move_down, 'Down')
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()






screen.exitonclick()