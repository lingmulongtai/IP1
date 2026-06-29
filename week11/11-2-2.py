"""Week 11 exercise 2.2: reverse a one-to-one map."""


e2j = {
    "one": "ichi",
    "two": "ni",
    "three": "san",
    "four": "yon",
    "five": "go",
}


def reverseMap(d):
    result = dict()
    for key in d:
        # 元の値を新しいキーにして、元のキーを新しい値にする。
        result[d[key]] = key
    return result


if __name__ == "__main__":
    print("EN to JA:", e2j)
    print("JA to EN:", reverseMap(e2j))
