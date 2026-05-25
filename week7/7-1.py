"""Week 7 exercise 1: wrapper functions for trig in degrees."""

import math


def sind(x):
    return math.sin(math.radians(x))


def cosd(x):
    return math.cos(math.radians(x))


def tand(x):
    return math.tan(math.radians(x))


if __name__ == "__main__":
    print(sind(0))    # 0.0
    print(sind(270))  # -1.0
    print(cosd(60))   # 0.5
    print(tand(45))   # 1.0
