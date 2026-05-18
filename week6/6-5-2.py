"""Week 6 challenge 5.2: print digits backwards (recursive)."""


def printNum(n):
    print(n % 10)
    if n >= 10:
        printNum(n // 10)


if __name__ == "__main__":
    printNum(3210)
