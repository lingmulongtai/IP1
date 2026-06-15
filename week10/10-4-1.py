"""Week 10 challenge 4.1: find interlocking word pairs."""


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
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())

    pairs = set()
    for word in words:
        if len(word) < 6:
            continue
        a = word[0::2]
        b = word[1::2]
        if len(a) >= 3 and len(b) >= 3:
            if includes(words, a) and includes(words, b):
                pair = tuple(sorted([a, b]))
                pairs.add(pair)

    for a, b in sorted(pairs):
        print(a, b)
    print("interlocking pairs:", len(pairs))
