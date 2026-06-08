"""Week 9 exercise 4.2: histogram of letter frequencies in words.txt."""

if __name__ == "__main__":
    for letter in "abcdefghijklmnopqrstuvwxyz":
        words = open("words.txt")
        count = 0
        for line in words:
            word = line.strip()
            count = count + word.count(letter)
        if count > 0:
            count = count + 1000
            print(letter, "*" * (count // 1000))
