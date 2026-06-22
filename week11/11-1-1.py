"""Week 11 exercise 1.1: create a histogram of a sequence."""


def histogram(seq):
    d = dict()
    for item in seq:
        if item not in d:
            d[item] = 0
        d[item] = d[item] + 1
    return d


if __name__ == "__main__":
    s = "peter piper picked a peck of pickled peppers"
    h = histogram(s)
    print(h)
