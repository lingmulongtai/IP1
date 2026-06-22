"""Week 9 exercise 4.3: histogram of word lengths (1 to 25) in words.txt."""

from pathlib import Path

if __name__ == "__main__":
    words_path = Path(__file__).with_name("words.txt")
    for length in range(1, 26):
        words = words_path.open()
        count = 0
        for line in words:
            word = line.strip()
            if len(word) == length:
                count = count + 1
        if count > 0:
            count = count + 1000
            print(length, "*" * (count // 1000))
