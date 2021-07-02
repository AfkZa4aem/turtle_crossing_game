from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(-240, 250)
        self.current_score = 1
        self.show_score()

    def show_score(self):
        self.write(f"Level: {self.current_score}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.clear()
        self.current_score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
