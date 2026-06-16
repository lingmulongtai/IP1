"""Week 10 exercise 2.3: birthday paradox simulation."""

from random import randint


def randlist(n, i, j):
    result = []
    for _ in range(n):
        result.append(randint(i, j))
    return result


def has_duplicates(l):
    sorted_l = sorted(l)
    for i in range(len(sorted_l) - 1):
        if sorted_l[i] == sorted_l[i + 1]:
            return True
    return False


def duplicate_percentage(n, trials=100000):
    count = 0
    for _ in range(trials):
        if has_duplicates(randlist(n, 1, 365)):
            count = count + 1
    return count / trials * 100


if __name__ == "__main__":
    trials = 100000

    for n in [22, 23, 40, 41]:
        print(f"n={n}: {duplicate_percentage(n, trials):.1f}%")

    min_50 = None
    min_90 = None
    for n in range(1, 70):
        pct = duplicate_percentage(n, trials)
        if min_50 is None and pct >= 50:
            min_50 = n
        if min_90 is None and pct >= 90:
            min_90 = n
        if min_50 is not None and min_90 is not None:
            break

    print()
    print(f"Minimum n for at least 50%: {min_50}")
    print(f"Minimum n for at least 90%: {min_90}")
    print(f"About {min_50} people for a 50% chance of a shared birthday")
    print(f"About {min_90} people for a 90% chance of a shared birthday")
