"""Week 10 exercise 3.3: reverse pairs using binary search (includes)."""


def includes(sequence, target):
    first = 0
    last = len(sequence) - 1
    while first <= last:
        # 真ん中を見て、探す範囲を毎回半分にする。
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
    # この.pyファイルと同じ場所にあるwords.txtを開く。
    with open(__file__.replace("10-3-3.py", "words.txt")) as f:
        for line in f:
            words.append(line.strip())

    for word in words:
        # 3.2と同じ探し方だが、inの代わりに二分探索を使う。
        revword = word[::-1]
        if includes(words, revword) and word < revword:
            print(word, revword)
