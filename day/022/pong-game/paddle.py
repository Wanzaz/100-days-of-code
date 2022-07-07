from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=5)
        self.goto(position)


    def go_up(self):
        """Allows the paddle to move up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Allows the paddle to move down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
