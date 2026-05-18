"""Week 6 challenge 5.4: print digits on one line."""


def printNum(n):
    if n >= 10:
        printNum(n // 10)
    print(n % 10, end="")


if __name__ == "__main__":
    printNum(3210)
    print()
