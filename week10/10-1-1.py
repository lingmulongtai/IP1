"""Week 10 exercise 1.1: total(numbers)."""


def total(numbers):
    result = 0
    for n in numbers:
        result = result + n
    return result


if __name__ == "__main__":
    print(total([1, 1, 1, 1, 1]))  # 5
    print(total([1, 2, 3, 4, 5]))  # 15
    print(total(range(10)))        # 45
