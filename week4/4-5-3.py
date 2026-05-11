"""Week 4 challenge 5.3: pad with default width/character."""


def pad(n, width=8, character=" "):
    s = str(n)
    return character * (width - len(s)) + s


print(pad(123456))
print(pad(123, 8, "."))
