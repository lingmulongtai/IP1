"""Week 3 challenge 6.4: limit of F_n / F_{n-1} (tends to golden ratio)."""

# Large n: ratio of successive Fibonacci numbers approaches a constant (~1.618...)
n = 80
fm2, fm1 = 0, 1
for _ in range(2, n + 1):
    fn = fm1 + fm2
    fm2, fm1 = fm1, fn
ratio = fm1 / fm2 if fm2 != 0 else float("nan")
print(f"F_{n}/F_{n-1} ~ {ratio}")
