"""Week 4 exercise 4: functions as first-class values."""


def twice(f, x):
    f(x)
    f(x)


twice(print, "hello")
