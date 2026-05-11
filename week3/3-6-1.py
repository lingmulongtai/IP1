"""Week 3 challenge 6.1: sum of first N counting numbers (flowchart)."""

N = int(input("N: "))
S = 0
while N > 0:
    S = S + N
    N = N - 1
print(S)
