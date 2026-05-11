"""Week 4 exercise 3: hierarchical decomposition for time formatting."""

import datetime


def pad(n):
    s = str(n)
    return "0" * (2 - len(s)) + s


def alarm_format(h, m, s):
    return pad(h) + ":" + pad(m) + ":" + pad(s)


def time_string():
    now = datetime.datetime.now()
    return alarm_format(now.hour, now.minute, now.second)


print(pad(""))
print(pad("2"))
print(pad(2))
print(pad("42"))
print(pad(42))

print(alarm_format(13, 2, 7))
print(time_string())
