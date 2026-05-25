"""Week 7 exercise 2.2: factorial with argument validation."""


def factorial(n):
    if not isinstance(n, int):
        print("argument must be an integer")
        return None
    if n < 0:
        print("argument must be non-negative")
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(5.5))
    print(factorial(-1))
    print(factorial("x"))
