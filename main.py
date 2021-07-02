from turtle import Turtle, Screen
from player import Player
from car import Car
from level import Level
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.tracer(0)

player = Player()
car = Car()
level = Level()

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move()
    # Detect collisions with cars
    for new_car in car.all_cars:
        if new_car.distance(player) < 20:
            level.game_over()
            game_is_on = False
    # Go to next level if passed
    if player.ycor() == 290:
        player.goto(0, -280)
        level.next_level()
        car.increase_score()

screen.exitonclick()
