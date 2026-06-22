"""Week 11 exercise 4.3: make a histogram of words in a file."""

from pathlib import Path


def isLetter(c):
    return c.isalpha() or c.isspace()


def depunctuate(word):
    return "".join(filter(isLetter, word))


def printAscending(d):
    for key in sorted(d):
        print(key, d[key])


if __name__ == "__main__":
    h = dict()
    text_path = Path(__file__).with_name("text2.txt")
    with text_path.open() as f:
        for line in f:
            line = depunctuate(line)
            for word in line.split():
                word = word.lower()
                h[word] = h.get(word, 0) + 1

    printAscending(h)
    print()
    print("do appears", h.get("do", 0), "times")
    print("know appears", h.get("know", 0), "times")
