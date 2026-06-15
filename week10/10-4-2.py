"""Week 10 challenge 4.2: find three-way interlocking word triples."""


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

    triples = set()
    for word in words:
        if len(word) < 9:
            continue
        a = word[0::3]
        b = word[1::3]
        c = word[2::3]
        if len(a) >= 3 and len(b) >= 3 and len(c) >= 3:
            if includes(words, a) and includes(words, b) and includes(words, c):
                triple = tuple(sorted([a, b, c]))
                triples.add(triple)

    for a, b, c in sorted(triples):
        print(a, b, c)
    print("three-way interlocking triples:", len(triples))
