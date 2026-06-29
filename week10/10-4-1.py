"""Week 10 challenge 4.1: find interlocking word pairs."""


def includes(sequence, target):
    first = 0
    last = len(sequence) - 1
    while first <= last:
        # words.txtはソート済みなので、二分探索でかなり速く探せる。
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
    with open(__file__.replace("10-4-1.py", "words.txt")) as f:
        for line in f:
            words.append(line.strip())

    count = 0
    for word in words:
        if len(word) < 6:
            continue

        # 偶数番目と奇数番目に分けると、interlocking元の2語になる。
        a = word[0::2]
        b = word[1::2]
        if len(a) >= 3 and len(b) >= 3:
            if includes(words, a) and includes(words, b):
                # 見つけた組をそのまま出す。最後に何組あったかも確認する。
                print(a, b)
                count = count + 1

    print("interlocking pairs:", count)
