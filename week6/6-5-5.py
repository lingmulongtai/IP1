"""Week 6 challenge 5.5: print in an arbitrary base."""


def printNum(n, b):
    if n >= b:
        printNum(n // b, b)
    print(n % b, end="")


if __name__ == "__main__":
    printNum(3210, 10)
    print()
    printNum(255, 8)
    print()
    printNum(42, 2)
    print()
