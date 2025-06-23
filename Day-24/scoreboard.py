from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_socre(self):
        self.score +=1
        self.clear()
        self.update_score()
