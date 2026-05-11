"""Week 3 challenge 6.3: Nth Fibonacci number (F0=0, F1=1)."""

N = int(input("N: "))
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    fm2, fm1 = 0, 1
    for _ in range(2, N + 1):
        fn = fm1 + fm2
        fm2, fm1 = fm1, fn
    print(fm1)
