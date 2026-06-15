"""Week 10 exercise 1.3: nested_sum(n)."""


def nested_sum(n):
    if type(n) is int:
        return n
    elif type(n) is list:
        result = 0
        for item in n:
            result = result + nested_sum(item)
        return result
    else:
        return 0


if __name__ == "__main__":
    print(nested_sum([None, 1, [2, "two", [[[[3, False, 4]]]], []], 5]))
