import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtler")
game_is_on = True

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_car()
    screen.update()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

        if player.finish_line():
            scoreboard.increase_level()
            player.goto(0, -280)
            car_manager.level_up()

screen.exitonclick()
