import time
from food import Food
from snake import Snake
from turtle import Screen
from score_board import ScoreBoard

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
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.18)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
        time.sleep(5)
        exit()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()



screen.exitonclick()

