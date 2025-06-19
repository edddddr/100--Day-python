import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
carManager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(turtle.go_up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_car()
    carManager.move()

    # Detect colisoion with car
    for car in carManager.all_car:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if turtle.is_at_finish_line():
        turtle.got_to_start()
        carManager.level_up()
        scoreboard.icrease_level()



screen.exitonclick()