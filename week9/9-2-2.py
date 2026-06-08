"""Week 9 exercise 2.2: print words in words.txt that use only acefhlo."""


def uses_only(word, letters):
    for ch in word:
        if ch not in letters:
            return False
    return True


if __name__ == "__main__":
    with open("words.txt") as words:
        for line in words:
            word = line.strip()
            if uses_only(word, "acefhlo"):
                print(word)
