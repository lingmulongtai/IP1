"""Week 11 exercise 1.2: print a dictionary in key order."""


def histogram(seq):
    d = dict()
    for item in seq:
        # 1.1と同じ数え方。後で並べて表示するために辞書で持つ。
        if item not in d:
            d[item] = 0
        d[item] = d[item] + 1
    return d


def printAscending(d):
    # sorted(d)は辞書のキーだけを昇順に並べてくれる。
    for key in sorted(d):
        print(key, d[key])


if __name__ == "__main__":
    d = {"b": 1, "c": 2, "a": 3}
    printAscending(d)

    print()
    s = "peter piper picked a peck of pickled peppers"
    h = histogram(s)
    printAscending(h)
