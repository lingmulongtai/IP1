"""Week 9 exercise 4.3: histogram of word lengths (1 to 25) in words.txt."""

if __name__ == "__main__":
    for length in range(1, 26):
        words = open("words.txt")
        count = 0
        for line in words:
            word = line.strip()
            if len(word) == length:
                count = count + 1
        if count > 0:
            count = count + 1000
            print(length, "*" * (count // 1000))
