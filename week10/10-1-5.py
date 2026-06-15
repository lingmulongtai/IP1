"""Week 10 exercise 1.5: is_anagram(a, b)."""


def is_anagram(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    print(is_anagram("tone", "note"))           # True
    print(is_anagram("chemical", "alchemic"))   # True
    print(is_anagram("detail", "dilate"))       # True
    print(is_anagram("angered", "enraged"))     # True
    print(is_anagram("tangled", "tingled"))     # False
    print(is_anagram("goat", "boat"))           # False
