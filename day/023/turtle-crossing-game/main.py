import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player, FINISH_LINE_Y

"""
Breake down the Problem:
    1. Move the turtle with keypress
    2. Create and move the cars
    3. Detect collision with car
    4. Detect when turtle reaches the other side
    5. Create a scoreboard
"""

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when a turtle collides with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing 
    if player.is_at_finish_line():
           player.go_to_start()
           car_manager.increase_speed()
           scoreboard.increase_level()


screen.exitonclick()

