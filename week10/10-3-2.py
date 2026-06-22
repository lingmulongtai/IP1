"""Week 10 exercise 3.2: find reverse pairs in words."""

from pathlib import Path

if __name__ == "__main__":
    words = []
    words_path = Path(__file__).with_name("words.txt")
    with words_path.open() as f:
        for line in f:
            words.append(line.strip())

    for word in words:
        revword = word[::-1]
        if revword in words and word < revword:
            print(word, revword)
