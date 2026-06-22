"""Week 10 exercise 3.3: reverse pairs using binary search (includes)."""

from pathlib import Path


def includes(sequence, target):
    first = 0
    last = len(sequence) - 1
    while first <= last:
        mid = (first + last) // 2
        elt = sequence[mid]
        if target < elt:
            last = mid - 1
        elif target > elt:
            first = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    words = []
    words_path = Path(__file__).with_name("words.txt")
    with words_path.open() as f:
        for line in f:
            words.append(line.strip())

    for word in words:
        revword = word[::-1]
        if includes(words, revword) and word < revword:
            print(word, revword)
