"""Week 11 exercise 4.3: make a histogram of words in a file."""


def isLetter(c):
    # depunctuateで使う判定。空白を残すとsplitしやすい。
    return c.isalpha() or c.isspace()


def depunctuate(word):
    return "".join(filter(isLetter, word))


def printAscending(d):
    for key in sorted(d):
        print(key, d[key])


if __name__ == "__main__":
    h = dict()
    # この.pyファイルと同じ場所にあるtext2.txtを開く。
    with open(__file__.replace("11-4-3.py", "text2.txt")) as f:
        for line in f:
            # 先に記号を消してから、単語ごとのリストに分ける。
            line = depunctuate(line)
            for word in line.split():
                # Doとdoを別単語にしないため、小文字にそろえる。
                word = word.lower()
                h[word] = h.get(word, 0) + 1

    printAscending(h)
    print()
    print("do appears", h.get("do", 0), "times")
    print("know appears", h.get("know", 0), "times")
