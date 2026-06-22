"""Week 11 exercise 2.2: reverse a one-to-one map."""


def reverseMap(d):
    result = dict()
    for key in d:
        result[d[key]] = key
    return result


if __name__ == "__main__":
    e2j = {
        "one": "ichi",
        "two": "ni",
        "three": "san",
        "four": "yon",
        "five": "go",
    }
    print("EN to JA:", e2j)
    print("JA to EN:", reverseMap(e2j))
