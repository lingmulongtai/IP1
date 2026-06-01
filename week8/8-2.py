"""Week 8 exercise 2: searching and counting characters in sequences."""


def find_letter(word, letter):
    i = 0
    while i < len(word):
        if word[i] == letter:
            return i
        i = i + 1
    return None


def find_letter1(word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            return i
    return None


def count_letter(word, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count = count + 1
    return count


def count_letters(word, letters):
    count = 0
    for ch in letters:
        for i in range(len(word)):
            if word[i] == ch:
                count = count + 1
    return count


if __name__ == "__main__":
    word = "abcdef"
    print("--- 2.1 find_letter ---")
    print(find_letter(word, "a"))  # 0
    print(find_letter(word, "f"))  # 5
    print(find_letter(word, "z"))  # None

    print("--- 2.2 find_letter1 (same as above) ---")
    print(find_letter1(word, "a"))
    print(find_letter1(word, "f"))
    print(find_letter1(word, "z"))

    word = "bananas"
    print("--- 2.3 count_letter ---")
    print(count_letter(word, "a"))  # 3
    print(count_letter(word, "n"))  # 2
    print(count_letter(word, "z"))  # 0

    print("--- 2.4 count_letters ---")
    print(count_letters(word, "a"))    # 3
    print(count_letters(word, "ban"))  # 6
    print(count_letters(word, "banz")) # 6
    print(count_letters(word, "bans")) # 7
