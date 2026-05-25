"""Week 7 exercise 3.1: sentinel value to end input."""

while True:
    s = input("n: ")
    if s == "stop":
        break
    n = int(s)
    print(n * 2)
