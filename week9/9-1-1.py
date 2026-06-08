"""Week 9 exercise 1.1: avoids(word, letters)."""


def avoids(word, letters):
    for ch in letters:
        if ch in word:
            return False
    return True


if __name__ == "__main__":
    print(avoids("cat", "ct"))         # False
    print(avoids("dog", "ct"))         # True
    print(avoids("chimpanzee", "ct"))  # False
    print(avoids("elephant", "ct"))    # False
    print(avoids("mongoose", "ct"))    # True
