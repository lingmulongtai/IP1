"""Week 7 exercise 2.1: factorial with call/return tracing."""


def factorial(n):
    print("factorial", n)
    if n == 0:
        print("returning result")
        return 1
    result = n * factorial(n - 1)
    print("returning result")
    return result


if __name__ == "__main__":
    print(factorial(5))  # 120
