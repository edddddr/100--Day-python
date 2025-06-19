from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        super().__init__()
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            y_position = randint(-280, 280)
            new_car.goto(300, y_position)
            self.all_car.append(new_car)
    
    def move(self):
        for car in self.all_car:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed+= MOVE_INCREMENT

    

    
     

        

