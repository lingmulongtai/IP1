"""Week 9 exercise 3.1: is_monotonic(word) and count in words.txt."""


def is_monotonic(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(is_monotonic("beefily"))    # True
    print(is_monotonic("beefiness"))  # False

    count = 0
    with open("words.txt") as words:
        for line in words:
            if is_monotonic(line.strip()):
                count = count + 1
    print("monotonic words:", count)
