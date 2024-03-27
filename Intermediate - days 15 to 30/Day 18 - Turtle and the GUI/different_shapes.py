from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
screen = Screen()


screen.bgcolor("black")
turtle.penup()
screen.colormode(255)
turtle.shape("turtle")
turtle.pensize(2)
turtle.goto(0, screen.window_height()//2 - 50)



def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(50)
        turtle.right(angle)

    
    
    


if __name__ == "__main__":
    turtle.pendown()
    input = int(input("How many shapes you want to draw? \t "))
    for shape_side_n in range(input+1,2,-1 ):
        shape_color = random_color()
        turtle.color(shape_color)
        turtle.fillcolor(shape_color)
        turtle.begin_fill()
        draw_shape(shape_side_n)
        turtle.end_fill()
    screen.exitonclick()