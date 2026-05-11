"""Week 4 exercise 2: left-padding to width 10."""


def justify(s):
    n = len(s)
    return " " * (10 - n) + s


print(justify("one"))
print(justify("two"))
print(justify("three"))
print(justify("four"))
print(justify("five"))
