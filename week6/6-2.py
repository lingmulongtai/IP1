"""Week 6 exercise 2: recursive functions."""


def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)


def sumOfCount(n):
    if n <= 0:
        return 0
    return n + sumOfCount(n - 1)


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    print("factorial(0..9):", [factorial(n) for n in range(10)])
    print("sumOfCount(0..9):", [sumOfCount(n) for n in range(10)])
    print("fibonacci(1..12):", [fibonacci(n) for n in range(1, 13)])
    print("gcd(24, 42) =", gcd(24, 42))
