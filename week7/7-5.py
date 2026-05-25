"""Week 7 challenge 5: table comparing newton() with math.sqrt()."""

import math


def newton(n, epsilon):
    s = n / 2
    while abs(s * s - n) >= n * epsilon:
        s = (s + n / s) / 2
    return s


def pad(s, width):
    s = str(s)
    if len(s) >= width:
        return s
    return s + " " * (width - len(s))


if __name__ == "__main__":
    epsilon = 1e-7

    print(pad("n", 10), pad("newton(n)", 25), pad("math.sqrt(n)", 20), pad("diff", 20))
    print(pad("-", 10), pad("---------", 25), pad("------------", 20), pad("----", 20))

    for n in range(1, 10):
        approx = newton(n, epsilon)
        exact = math.sqrt(n)
        diff = abs(approx - exact)
        print(
            pad(n, 10),
            pad(approx, 25),
            pad(exact, 20),
            pad(diff, 20),
        )
