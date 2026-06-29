"""Week 10 challenge 4.2: find three-way interlocking word triples."""


def includes(sequence, target):
    first = 0
    last = len(sequence) - 1
    while first <= last:
        # ここも4.1と同じ二分探索を使い回している。
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
    with open(__file__.replace("10-4-2.py", "words.txt")) as f:
        for line in f:
            words.append(line.strip())

    count = 0
    for word in words:
        if len(word) < 9:
            continue

        # 3-wayなので、0番目・1番目・2番目から3文字おきに切り出す。
        a = word[0::3]
        b = word[1::3]
        c = word[2::3]
        if len(a) >= 3 and len(b) >= 3 and len(c) >= 3:
            if includes(words, a) and includes(words, b) and includes(words, c):
                # 3つとも単語なら、その場で印刷して数える。
                print(a, b, c)
                count = count + 1

    print("three-way interlocking triples:", count)
