"""Week 6 exercise 4: Koch snowflake."""

import math
import turtle

def koch(x):
    if x < 3:
        turtle.forward(x)
        return
    koch(x / 3)
    turtle.left(60)
    koch(x / 3)
    turtle.right(120)
    koch(x / 3)
    turtle.left(60)
    koch(x / 3)


def snowflake(length):
    for _ in range(3):
        koch(length)
        turtle.right(120)


if __name__ == "__main__":
    length = 300
    screen = turtle.Screen()
    screen.tracer(100, 0)
    turtle.speed(0)
    turtle.hideturtle()
    # Three Koch sides form an equilateral triangle; its centroid is at the origin.
    turtle.penup()
    turtle.goto(-length / 2, length * math.sqrt(3) / 6)
    turtle.setheading(0)
    turtle.pendown()
    snowflake(length)
    screen.update()
    turtle.done()