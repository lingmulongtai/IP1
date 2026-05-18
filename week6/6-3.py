"""Week 6 exercise 3: Koch curve (recursive geometry)."""

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
    turtle.speed(0)
    turtle.hideturtle()
    koch(729)
    turtle.done()
