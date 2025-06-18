from turtle import Turtle, Screen 

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong ⚾⚾⚾")
screen.tracer(0)


paddle1 = Turtle('square')
paddle1.color('white')
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.setpos(350, 0)

def move_up():
    y_position = paddle1.ycor() + 20
    paddle1.goto(paddle1.xcor(), y_position)

def move_down():
    y_position = paddle1.ycor() - 20
    paddle1.goto(paddle1.xcor(), y_position)


screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()






screen.exitonclick()