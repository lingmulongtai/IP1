"""Week 10 exercise 2.2: has_duplicates(l)."""


def has_duplicates(l):
    sorted_l = sorted(l)
    for i in range(len(sorted_l) - 1):
        if sorted_l[i] == sorted_l[i + 1]:
            return True
    return False


if __name__ == "__main__":
    print(has_duplicates([1, 2, 3]))     # False
    print(has_duplicates([1, 1, 2, 3])) # True
    print(has_duplicates([1, 2, 2, 3])) # True
    print(has_duplicates([1, 2, 3, 3])) # True
    print(has_duplicates([1, 2, 3, 1])) # True
