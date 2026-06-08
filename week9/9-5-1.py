"""Week 9 challenge 5.1: count words in text.txt."""

if __name__ == "__main__":
    count = 0
    with open("text.txt") as text:
        for line in text:
            in_word = False
            for ch in line:
                if ch.isalpha():
                    if not in_word:
                        count = count + 1
                        in_word = True
                else:
                    in_word = False
    print(count)
