"""Week 10 exercise 3.1: read words.txt into a list."""

if __name__ == "__main__":
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())
    print("words loaded:", len(words))
    print("first word:", words[0])
    print("last word:", words[-1])
