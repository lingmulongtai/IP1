"""Week 11 exercise 1.2: print a dictionary in key order."""


def histogram(seq):
    d = dict()
    for item in seq:
        if item not in d:
            d[item] = 0
        d[item] = d[item] + 1
    return d


def printAscending(d):
    for key in sorted(d):
        print(key, d[key])


if __name__ == "__main__":
    d = {"b": 1, "c": 2, "a": 3}
    printAscending(d)

    print()
    s = "peter piper picked a peck of pickled peppers"
    h = histogram(s)
    printAscending(h)
