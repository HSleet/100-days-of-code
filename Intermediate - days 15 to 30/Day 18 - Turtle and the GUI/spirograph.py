from turtle import Turtle, Screen
from random import randint


SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000

turtle = Turtle()
screen = Screen()

screen.bgcolor("black")
screen.colormode(255)

turtle.speed(0)
steps = 60


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


for i in range(steps):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(turtle.heading() + 360/steps)


screen.exitonclick()