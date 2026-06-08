"""Week 9 exercise 2.1: uses_only(word, letters)."""


def uses_only(word, letters):
    for ch in word:
        if ch not in letters:
            return False
    return True


if __name__ == "__main__":
    print(uses_only("appeal", "aple"))      # True
    print(uses_only("apple", "aple"))       # True
    print(uses_only("apples", "aple"))      # False
    print(uses_only("lapel", "aple"))       # True
    print(uses_only("palpable", "aple"))    # False
    print(uses_only("palpable", "abple"))   # True
