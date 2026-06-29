"""Week 10 exercise 1.4: is_ordered(things)."""


def is_ordered(things):
    # 並び順は、隣同士だけ見れば崩れている場所を見つけられる。
    for i in range(len(things) - 1):
        if things[i] > things[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(is_ordered([]))                                           # True
    print(is_ordered([1, 1, 1]))                                    # True
    print(is_ordered([1, 2, 3]))                                    # True
    print(is_ordered([1, 3, 2]))                                    # False
    print(is_ordered([2, 1, 3]))                                    # False
    print(is_ordered([[1], [2]]))                                   # True
    print(is_ordered([[2], [1]]))                                   # False
    print(is_ordered(["any", "body", "can", "dance", "even", "fred"]))  # True
