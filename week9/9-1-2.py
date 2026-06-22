"""Week 9 exercise 1.2: count words in words.txt that avoid forbidden letters."""

from pathlib import Path


def avoids(word, letters):
    for ch in letters:
        if ch in word:
            return False
    return True


def count_avoiding(forbidden):
    count = 0
    words_path = Path(__file__).with_name("words.txt")
    with words_path.open() as words:
        for line in words:
            if avoids(line.strip(), forbidden):
                count = count + 1
    return count


if __name__ == "__main__":
    forbidden = input("Enter forbidden letters: ")
    print(count_avoiding(forbidden))
