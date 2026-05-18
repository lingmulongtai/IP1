"""Week 6 exercise 3: Koch curve (recursive geometry)."""

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


if __name__ == "__main__":
    length = 729
    screen = turtle.Screen()
    screen.tracer(0)
    screen.delay(0)
    turtle.speed(0)
    turtle.hideturtle()
    # Chord length is `length`; peak height is length * sqrt(3) / 6 above the baseline.
    turtle.penup()
    turtle.goto(-length / 2, -length * math.sqrt(3) / 12)
    turtle.setheading(0)
    turtle.pendown()
    koch(length)
    screen.update()
    turtle.done()