"""Week 8 exercise 4 (challenge): rotational cipher rotate(string, n)."""


def rotate(string, n):
    r = ""
    for c in string:
        if "a" <= c <= "z":
            pos = (ord(c) - ord("a") + n) % 26
            r += chr(ord("a") + pos)
        elif "A" <= c <= "Z":
            pos = (ord(c) - ord("A") + n) % 26
            r += chr(ord("A") + pos)
        else:
            r += c
    return r


if __name__ == "__main__":
    print(rotate("abcxyz", 2))   # cdezab
    print(rotate("abcxyz", -1))  # zabwxy

    # step 3 check: positions for "pineapplez" +1 end with 0 not 26
    for c in "pineapplez":
        print((ord(c) - ord("a") + 1) % 26, end=" ")
    print()

    print(rotate("abc 123", 2))  # cde 123

    msg = "This is a message that has been encoded."
    encoded = rotate(msg, 13)
    print(encoded)
    print(rotate(encoded, -13) == msg)

    s = "hello"
    print(rotate(rotate(s, 5), -5) == s)
