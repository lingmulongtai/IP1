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

    for n in range(1, 50):
        pct = duplicate_percentage(n, trials)
        print(f"n={n}: {pct:.1f}%")

    print()
    for n in range(1, 50):
        if duplicate_percentage(n, trials) >= 50:
            print(f"Minimum n for at least 50%: {n}")
            break

    print(f"50% chance of shared birthday: about 23 people")
    print(f"90% chance of shared birthday: about 41 people")
