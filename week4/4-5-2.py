"""Week 4 challenge 5.2: general pad(n, width, character)."""


def pad(n, width, character):
    s = str(n)
    return character * (width - len(s)) + s


print(pad("hello", 10, " "))
print(pad("", 2, "0"))
print(pad(4, 2, "0"))
print(pad(42, 2, "0"))
print(pad("", 8, "-"))
print(pad(123, 8, "."))
print(pad(456789, 8, "0"))
