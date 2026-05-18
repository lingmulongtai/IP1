"""Week 6 challenge 5.3: print digits forwards (recursive)."""


def printNum(n):
    if n >= 10:
        printNum(n // 10)
    print(n % 10)


if __name__ == "__main__":
    printNum(3210)
