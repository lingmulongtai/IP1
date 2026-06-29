"""Week 11 exercise 4.1: identify letters and spaces."""


def isLetter(c):
    # 単語の区切りに必要な空白だけは、文字ではなくても残す。
    return c.isalpha() or c.isspace()


if __name__ == "__main__":
    print(isLetter("a"))  # True
    print(isLetter("B"))  # True
    print(isLetter(" "))  # True
    print(isLetter(","))  # False
    print(isLetter("."))  # False
