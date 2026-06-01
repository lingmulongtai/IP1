"""Week 8 exercise 3: palindromes."""


def palindrome(string):
    length = len(string)
    for i in range(length):
        if string[i] != string[length - 1 - i]:
            return False
    return True


def palindrome1(s):
    return s == s[::-1]


if __name__ == "__main__":
    for w in ("reviver", "level", "deed", "banana", "lever"):
        print(w, palindrome(w), palindrome1(w))
