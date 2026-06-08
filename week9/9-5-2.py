"""Week 9 challenge 5.2: count lines, words, and characters in text.txt."""

if __name__ == "__main__":
    lines = 0
    words = 0
    chars = 0
    with open("text.txt") as text:
        for line in text:
            lines = lines + 1
            chars = chars + len(line)
            in_word = False
            for ch in line:
                if ch.isalpha():
                    if not in_word:
                        words = words + 1
                        in_word = True
                else:
                    in_word = False
    print("lines:", lines)
    print("words:", words)
    print("characters:", chars)
