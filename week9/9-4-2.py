"""Week 9 exercise 4.2: histogram of letter frequencies in words.txt."""

from pathlib import Path

if __name__ == "__main__":
    words_path = Path(__file__).with_name("words.txt")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        words = words_path.open()
        count = 0
        for line in words:
            word = line.strip()
            count = count + word.count(letter)
        if count > 0:
            count = count + 1000
            print(letter, "*" * (count // 1000))
