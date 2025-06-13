from turtle import Turtle, Screen
import random

is_race_start = False


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color : ")
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange'] 
Y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(len(colors)):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=Y_position[turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race_start = True

while is_race_start:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_start = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()






# My solution
# tim = Turtle(shape='turtle')
# # tim.color(colors[0])
# tom = Turtle(shape='turtle')
# # tom.color(colors[1])
# tot = Turtle(shape='turtle')
# # tot.color(colors[2])
# moti = Turtle(shape='turtle')
# # moti.color(colors[3])
# moi = Turtle(shape='turtle')
# # moi.color(colors[4])
# momi = Turtle(shape='turtle')
# # momi.color(colors[5])

# turtles_name = [tim, tom, tot, moti, moi, momi]
# for n in range(len(colors)):
#     turtles_name[n].color(colors[n])
#     turtles_name[n].penup()
# tim.penup()
# tim.goto(x=-230, y=-100)
# tom.goto(x=-230, y=-50)
# tot.goto(x=-230, y=-10)
# moti.goto(x=-230, y=30)
# moi.goto(x=-230, y=60)
# momi.goto(x=-230, y=100)
