"""Week 9 exercise 2.2: print words in words.txt that use only acefhlo."""

from pathlib import Path


def uses_only(word, letters):
    for ch in word:
        if ch not in letters:
            return False
    return True


if __name__ == "__main__":
    words_path = Path(__file__).with_name("words.txt")
    with words_path.open() as words:
        for line in words:
            word = line.strip()
            if uses_only(word, "acefhlo"):
                print(word)
