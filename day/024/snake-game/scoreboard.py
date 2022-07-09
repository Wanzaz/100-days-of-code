from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        with open("data.txt", mode="r") as file:
            data = file.read() 
            self.high_score = [int(i) for i in data if i.isdigit()]
            if self.score > self.high_score[0]:
                with open("data.txt", mode="w") as file:
                    file.write(f"{self.score}")
        self.update_scoreboard()
        self.score = 0

    def reset_start(self):
        with open("data.txt", mode="r") as file:
            data = file.read() 
            self.high_score = [int(i) for i in data if i.isdigit()]
            if self.score > self.high_score[0]:
                with open("data.txt", mode="w") as file:
                    file.write(f"{self.score}")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

