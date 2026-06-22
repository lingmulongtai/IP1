"""Week 9 challenge 5.2: count lines, words, and characters in text.txt."""

from pathlib import Path

if __name__ == "__main__":
    lines = 0
    words = 0
    chars = 0
    text_path = Path(__file__).with_name("text.txt")
    with text_path.open() as text:
        for line in text:
            lines = lines + 1
            chars = chars + len(line)
            in_word = False
            for ch in line:
                if ch.isalpha():
                    if not in_word:
                        words = words + 1
                        in_word = True
                else:
                    in_word = False
    print("lines:", lines)
    print("words:", words)
    print("characters:", chars)
