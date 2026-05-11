"""Week 5 exercise 4.1: square from four triangles (bonus pattern)."""

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
    turtle.right(90 - angle_deg / 2)


def pattern_square(side):
    equal_side = side * math.sqrt(2) / 2
    apex_angle = 90
    for _ in range(4):
        triangle(equal_side, apex_angle)
        turtle.left(90)


if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    pattern_square(160)
    turtle.done()
