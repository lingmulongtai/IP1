"""Week 6 exercise 1: conditional statements."""


def isDivisibleBy(n, m):
    return n % m == 0


def evenOdd(n):
    if isDivisibleBy(n, 2):
        return "even"
    return "odd"


def ageGroup(age):
    if age < 6:
        return "baby"
    elif age < 18:
        return "school"
    elif age < 22:
        return "student"
    elif age < 65:
        return "employed"
    return "retired"


if __name__ == "__main__":
    print("--- 1.1 part 1: even / odd ---")
    for i in range(10):
        print(i, evenOdd(i))

    print("--- 1.1 part 3: divisible by 7 (0..100) ---")
    for n in range(101):
        if isDivisibleBy(n, 7):
            print(n)

    print("--- 1.2: age groups (0..69) ---")
    for age in range(70):
        print(age, ageGroup(age))
