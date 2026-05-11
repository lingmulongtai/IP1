"""Week 3 exercise 3: movie length in minutes → hours and minutes."""

m = int(input("minutes: "))
h = int(m // 60)
m = m - 60 * h
print(f"{h} hours {m} minutes")
