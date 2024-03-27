import turtle as t
from random import choice
import colorgram


colors  = colorgram.extract('C:\\Users\\jemen\\Documents\\GitHub\\100 days of code\\Intermediate - days 15 to 30\\Day 18 - Turtle and the GUI\\hirst-1.webp', 50)

COLUMNS_COUNT = 15
ROWS_COUNT = 12
DISTANCE = 40

pen = t.Turtle()
screen = t.Screen()

pen.speed(0)
pen.penup()
screen.colormode(255)
screen.setup(width=800, height=600)

pen.setpos(-375, 275)

def draw_color(color):
    pen.dot(15, color.rgb)
    pen.forward(DISTANCE)


def draw_row(colors):
    for _ in range(COLUMNS_COUNT):
        draw_color(choice(colors))
    pen.setpos(-375, pen.ycor() - DISTANCE)
    

def draw(rows, colors):
    for _ in range(rows):
        draw_row(colors)


if __name__ == "__main__":
    draw(ROWS_COUNT, colors)
    screen.exitonclick()

