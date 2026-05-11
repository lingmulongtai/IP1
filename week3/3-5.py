"""Week 3 exercise 5: dot product of two 2D vectors (tuples)."""

s_a = input("vector A: ")
s_b = input("vector B: ")
A = eval(s_a)
B = eval(s_b)
dot = A[0] * B[0] + A[1] * B[1]
print(f"{A} . {B} = {dot}")
