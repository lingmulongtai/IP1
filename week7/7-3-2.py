"""Week 7 exercise 3.2: running total and average with sentinel."""

total = 0
count = 0

while True:
    s = input("n: ")
    if s == "stop":
        break
    n = int(s)
    total += n
    count += 1
    print(n * 2)
    print("total:", total, "average:", total / count)
