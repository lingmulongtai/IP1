"""Week 9 exercise 3.2: words with three consecutive double letters."""

from pathlib import Path


def is_double(word, position):
    return word[position] == word[position + 1]


def has_triple_double(word):
    for i in range(len(word) - 5):
        if is_double(word, i) and is_double(word, i + 2) and is_double(word, i + 4):
            return True
    return False


if __name__ == "__main__":
    words_path = Path(__file__).with_name("words.txt")
    with words_path.open() as words:
        for line in words:
            word = line.strip()
            if has_triple_double(word):
                print(word)
