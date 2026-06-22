"""Week 9 challenge 5.1: count words in text.txt."""

from pathlib import Path

if __name__ == "__main__":
    count = 0
    text_path = Path(__file__).with_name("text.txt")
    with text_path.open() as text:
        for line in text:
            in_word = False
            for ch in line:
                if ch.isalpha():
                    if not in_word:
                        count = count + 1
                        in_word = True
                else:
                    in_word = False
    print(count)
