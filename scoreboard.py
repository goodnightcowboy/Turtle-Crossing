from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = 'left'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("Black")
        self.goto(x=-280, y=250)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 40, 'normal'))
