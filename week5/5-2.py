"""Week 5 exercise 2: petal and flower."""

import turtle


def arc(radius, angle):
    turtle.circle(radius, angle)


def petal(radius, angle):
    for _ in range(2):
        arc(radius, angle)
        turtle.left(180 - angle)


def flower(radius, angle, npetals):
    for _ in range(npetals):
        petal(radius, angle)
        turtle.left(360 / npetals)


if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    flower(200, 40, 10)
    turtle.done()
