import time
from turtle import Screen
from snake import Snake

"""
Parts of this project
1. Snake body
2. Move the snake
3. Create snake food
4. Detect collision with food
5. Create a scoreboard
6. Detect collision with wall
7. Detect collision with tail
"""

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()



screen.exitonclick()

