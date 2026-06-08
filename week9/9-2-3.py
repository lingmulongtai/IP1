"""Week 9 exercise 2.3: uses_all(word, letters)."""


def uses_all(word, letters):
    return all(ch in word for ch in letters)


if __name__ == "__main__":
    print(uses_all("banana", "ban"))   # True
    print(uses_all("banana", "abn"))   # True
    print(uses_all("banana", "xyz"))   # False
