from turtle import Turtle
import random

COLOR = ["red", "yellow", "blue", "green", "purple", "orange"]
X_COR = 300


class Car:

    def __init__(self):
        self.all_cars = []
        self.starting_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLOR))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(X_COR, random.randrange(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.starting_speed)

    def increase_score(self):
        self.starting_speed += 5
