from turtle import Turtle
SEGMENT_POSITION = [(0, 0), (20, 0), (40, 0)]
DISTANCE = 20
UP = 20
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """"Create a new 3 sgments"""
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]
       
    def create_snake(self):
         for postion in SEGMENT_POSITION:
            new_position = Turtle(shape='square')
            new_position.color("white")
            new_position.penup()
            new_position.goto(postion)
            self.segments.append(new_position)


    def move(self):
        """"Start moveing snake"""
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.haed.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.haed.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.haed.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.haed.heading() != LEFT:
            self.head.setheading(RIGHT)
