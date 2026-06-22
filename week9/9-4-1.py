"""Week 9 exercise 4.1: average word length in words.txt."""

from pathlib import Path

if __name__ == "__main__":
    total = 0
    count = 0
    words_path = Path(__file__).with_name("words.txt")
    with words_path.open() as words:
        for line in words:
            word = line.strip()
            total = total + len(word)
            count = count + 1
    print(round(total / count, 1))
