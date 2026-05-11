"""Week 3 challenge 6.2: factorial N! (assume N >= 1)."""

N = int(input("N: "))
F = 1
while N > 1:
    F = F * N
    N = N - 1
print(F)
