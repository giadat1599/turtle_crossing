from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

game_is_on = True
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=player.move)

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_y():
        player.reset()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
