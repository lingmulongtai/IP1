"""Week 10 exercise 3.1: read words.txt into a list."""

from pathlib import Path

if __name__ == "__main__":
    words = []
    words_path = Path(__file__).with_name("words.txt")
    with words_path.open() as f:
        for line in f:
            words.append(line.strip())
    print("words loaded:", len(words))
    print("first word:", words[0])
    print("last word:", words[-1])
