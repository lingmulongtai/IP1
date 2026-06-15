"""Week 10 exercise 3.2: find reverse pairs in words."""

if __name__ == "__main__":
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())

    for word in words:
        revword = word[::-1]
        if revword in words and word < revword:
            print(word, revword)
