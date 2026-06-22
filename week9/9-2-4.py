"""Week 9 exercise 2.4: count words using all vowels aeiou / aeiouy."""

from pathlib import Path


def uses_all(word, letters):
    return all(ch in word for ch in letters)


if __name__ == "__main__":
    aeiou = 0
    aeiouy = 0
    words_path = Path(__file__).with_name("words.txt")
    with words_path.open() as words:
        for line in words:
            word = line.strip()
            if uses_all(word, "aeiou"):
                aeiou = aeiou + 1
            if uses_all(word, "aeiouy"):
                aeiouy = aeiouy + 1
    print("aeiou:", aeiou)
    print("aeiouy:", aeiouy)
