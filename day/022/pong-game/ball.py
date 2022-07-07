from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        #self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Increases X and Y numbers per 10 each time"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):            
        """The Y number becomes negative"""
        self.y_move *= -1

    def bounce_x(self):            
        """The X number becomes negative"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_positition(self):
        """Reset the ball's postition to center of the screen. The ball starts moving towards the other player"""
        self.home()
        self.move_speed = 0.1
        self.bounce_x()

