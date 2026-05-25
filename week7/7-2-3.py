"""Week 7 exercise 2.3: factorial — validate only on the outer call."""


def factorial(n):
    if not isinstance(n, int):
        print("argument must be an integer")
        return None
    if n < 0:
        print("argument must be non-negative")
        return None
    return _factorial(n)


def _factorial(n):
    if n == 0:
        return 1
    return n * _factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(5.5))
    print(factorial(-1))
    print(factorial("x"))
