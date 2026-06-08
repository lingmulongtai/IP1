"""Week 9 exercise 1.2: count words in words.txt that avoid forbidden letters."""


def avoids(word, letters):
    for ch in letters:
        if ch in word:
            return False
    return True


def count_avoiding(forbidden):
    count = 0
    with open("words.txt") as words:
        for line in words:
            if avoids(line.strip(), forbidden):
                count = count + 1
    return count


if __name__ == "__main__":
    forbidden = input("Enter forbidden letters: ")
    print(count_avoiding(forbidden))
