"""Week 11 exercise 4.2: remove punctuation from text."""

from pathlib import Path


def isLetter(c):
    return c.isalpha() or c.isspace()


def depunctuate(word):
    return "".join(filter(isLetter, word))


if __name__ == "__main__":
    text_path = Path(__file__).with_name("text2.txt")
    with text_path.open() as f:
        for line in f:
            print(depunctuate(line), end="")
