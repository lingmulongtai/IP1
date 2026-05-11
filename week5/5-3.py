"""Week 5 exercise 3: isosceles triangle and pizza."""

import math
import turtle


def triangle(length, angle):
    angle_deg = angle
    base_angle = (180 - angle_deg) / 2
    half_base = length * math.sin(math.radians(angle_deg) / 2)
    turtle.left(90 - angle_deg / 2)
    turtle.forward(length)
    turtle.left(180 - base_angle)
    turtle.forward(2 * half_base)
    turtle.left(180 - base_angle)
    turtle.forward(length)
    turtle.left(90 - angle_deg / 2)


def pizza(length, number):
    wedge = 360 / number
    turtle.setheading(wedge / 2)
    for _ in range(number):
        triangle(length, wedge)
        turtle.left(wedge)


if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    pizza(100, 8)
    turtle.done()
