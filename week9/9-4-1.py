"""Week 9 exercise 4.1: average word length in words.txt."""

if __name__ == "__main__":
    total = 0
    count = 0
    with open("words.txt") as words:
        for line in words:
            word = line.strip()
            total = total + len(word)
            count = count + 1
    print(round(total / count, 1))
