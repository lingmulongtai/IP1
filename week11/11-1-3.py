"""Week 11 exercise 1.3: display a histogram as a bar chart."""


def histogram(seq):
    d = dict()
    for item in seq:
        # 文字をキー、出てきた回数を値として記録する。
        if item not in d:
            d[item] = 0
        d[item] = d[item] + 1
    return d


def printHistogram(d):
    for key in sorted(d):
        # 回数ぶんだけ*をくり返すと、簡単な棒グラフになる。
        print(key, "*" * d[key])


if __name__ == "__main__":
    d = {"b": 1, "c": 2, "a": 3}
    printHistogram(d)

    print()
    s = "peter piper picked a peck of pickled peppers"
    h = histogram(s)
    printHistogram(h)
