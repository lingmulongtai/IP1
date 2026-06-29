"""Week 10 exercise 2.1: randlist(n, i, j)."""

from random import randint


def randlist(n, i, j):
    result = []
    # n回だけ乱数を作り、appendで後ろへ足していく。
    for _ in range(n):
        result.append(randint(i, j))
    return result


if __name__ == "__main__":
    print(randlist(10, 1, 5))
