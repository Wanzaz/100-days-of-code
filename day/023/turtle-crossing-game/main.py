import time
import signal
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")


counter = 0
game_is_on = True
while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()

    # Detect when a turtle collides with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            signal.pause()
            time.sleep(3)
            exit()

    # Detect when a turtle player has reached the top of the screen
    #if player.ycor() > player.FINISH_LINE_Y:
    #   player.reset_position()


    car_manager.create_car()

    car_manager.move_cars()
