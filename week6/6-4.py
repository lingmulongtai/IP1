"""Week 6 exercise 4: Koch snowflake."""

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
    turtle.speed(0)
    turtle.hideturtle()
    snowflake(300)
    turtle.done()
