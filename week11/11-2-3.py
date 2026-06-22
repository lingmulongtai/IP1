"""Week 11 exercise 2.3: reverse a many-to-one map."""


def histogram(seq):
    d = dict()
    for item in seq:
        d[item] = d.get(item, 0) + 1
    return d


def printAscending(d):
    for key in sorted(d):
        print(key, d[key])


def reverseMap(d):
    result = dict()
    for key in d:
        value = d[key]
        if value not in result:
            result[value] = []
        result[value].append(key)
    return result


if __name__ == "__main__":
    s = "peter piper picked a peck of pickled peppers"
    h = histogram(s)
    print("Histogram:")
    print(h)
    print("Reverse map:")
    printAscending(reverseMap(h))
