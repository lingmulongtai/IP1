"""Week 6 challenge 5.8: default base, width, and padding."""


def printNum(n, b=10, w=1, p=" "):
    if w == 0:
        if n >= b:
            printNum(n // b, b, 0, p)
        print(n % b, end="")
        return
    if w > 1:
        if n >= b:
            printNum(n // b, b, w - 1, p)
        else:
            print(p, end="")
            printNum(n, b, w - 1, p)
            return
    print(n % b, end="")


if __name__ == "__main__":
    printNum(3210, 10, 0)
    print()
    printNum(255, 8, 3)
    print()
    printNum(255, 8, 4)
    print()
    printNum(42, 2, 8)
    print()
    printNum(3210, 10, 8, ".")
    print()
    printNum(255, 8, 8, " ")
    print()
    printNum(42, 2, 8, "0")
    print()
