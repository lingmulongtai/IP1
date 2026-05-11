"""Week 3 exercise 4: right triangle — hypotenuse and area."""

import math

a = float(input("a: "))
b = float(input("b: "))
hyp = math.hypot(a, b)
area = a * b / 2
print(f"hypotenuse {hyp} area {area}")
