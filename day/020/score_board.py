from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 23, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(0, 270)
        self.write(f"Score : {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

