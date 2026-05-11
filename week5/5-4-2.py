"""Week 5 exercise 4.2: sine wave with goto."""

import math
import turtle


def sine_wave_four_cycles():
    steps = 400
    turtle.up()
    for i in range(steps + 1):
        t = i / steps
        x = -200 + 400 * t
        angle = -2 * math.pi + 8 * math.pi * t
        y = 100 * math.sin(angle)
        turtle.goto(x, y)
        turtle.down()


if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    sine_wave_four_cycles()
    turtle.done()
