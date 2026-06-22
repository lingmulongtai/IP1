"""Week 11 exercise 1.4: create a histogram using dict.get()."""


def histogram(seq):
    d = dict()
    for item in seq:
        d[item] = d.get(item, 0) + 1
    return d


if __name__ == "__main__":
    s = "peter piper picked a peck of pickled peppers"
    h = histogram(s)
    print(h)
