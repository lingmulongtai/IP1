"""Week 5 exercise 4.3: plot arbitrary f(angle) and Fourier partial sum."""

import math
import turtle


def plot_function(f, steps=400, y_scale=100, y_shift=0):
    turtle.up()
    for i in range(steps + 1):
        t = i / steps
        x = -200 + 400 * t
        angle = -2 * math.pi + 4 * math.pi * t
        y = y_shift + y_scale * f(angle)
        turtle.goto(x, y)
        turtle.down()


def f_sum_odd_harmonics(angle, max_k):
    s = 0.0
    k = 1
    while k <= max_k:
        s += math.sin(k * angle) / k
        k += 2
    return s


if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()

    def f1(a):
        return math.sin(a)

    def f2(a):
        return math.sin(a) + (1 / 3) * math.sin(3 * a)

    def f3(a):
        return math.sin(a) + (1 / 3) * math.sin(3 * a) + (1 / 5) * math.sin(5 * a)

    def f99(a):
        return f_sum_odd_harmonics(a, 99)

    turtle.color("blue")
    plot_function(f1, y_shift=220)
    turtle.up()
    turtle.color("green")
    plot_function(f2, y_shift=80)
    turtle.up()
    turtle.color("orange")
    plot_function(f3, y_shift=-80)
    turtle.up()
    turtle.color("red")
    plot_function(f99, y_shift=-220)
    turtle.done()
