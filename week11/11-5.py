"""Week 11 challenge 5: count lines, words, and characters."""

from pathlib import Path


if __name__ == "__main__":
    lines = 0
    words = 0
    characters = 0

    text_path = Path(__file__).with_name("text2.txt")
    with text_path.open() as f:
        for line in f:
            lines = lines + 1
            words = words + len(line.split())
            characters = characters + len(line)

    print("lines:", lines)
    print("words:", words)
    print("characters:", characters)
