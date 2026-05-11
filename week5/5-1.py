"""Week 5 exercise 1: square with circles at corners."""

import turtle


def circle(radius):
    turtle.circle(radius)


def squareCircles(length, radius):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(135)
        circle(radius)
        turtle.right(135)


if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    squareCircles(160, 35)
    turtle.done()
