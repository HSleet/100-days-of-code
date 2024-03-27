from random import randint
from turtle import Turtle, Screen


STEP_SIZE = 100
SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000

left_border = -SCREEN_WIDTH // 2
right_border = SCREEN_WIDTH // 2
top_border = SCREEN_HEIGHT // 2
bottom_border = -SCREEN_HEIGHT // 2

vertical_line_qty = SCREEN_WIDTH // STEP_SIZE
horizontal_line_qty = SCREEN_HEIGHT // STEP_SIZE

turtle = Turtle()
screen = Screen()

screen.bgcolor("black")
screen.colormode(255)

turtle.speed(0)

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Random Walk")



def move_top_left():
    turtle.penup()
    turtle.goto(left_border, top_border)
    turtle.pendown()

def quad_draw():
    for _ in range(4):
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        
def draw_grid():
    turtle.pensize(1)
    for _ in range(horizontal_line_qty):
        for _ in range(vertical_line_qty):
            turtle.color(93,93,93)
            quad_draw()
            turtle.penup()
            turtle.forward(STEP_SIZE)
            turtle.pendown()
        turtle.penup()
        turtle.goto(left_border, turtle.ycor() - STEP_SIZE)
        turtle.pendown()
        turtle.setheading(0)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def random_walk():
    for i in range(200):
        turtle.pensize(i//10 + 1)
        turtle.color(random_color())
        turtle.forward(100)
        turtle.setheading(randint(0, 360))
        
if __name__ == "__main__":
    move_top_left()
    draw_grid()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    random_walk()
    screen.exitonclick()
    