"""Week 3 exercise 1: use Python as a calculator."""

from math import pi

# 1. Seconds in 42 minutes 42 seconds
seconds = 42 * 60 + 42
print("1. seconds in 42 min 42 s:", seconds)

# 2. Circumference c = 2πr, r = 5
r = 5
circumference = 2 * pi * r
print("2. circumference (r=5):", circumference)

# 3. Area a = πr², r = 5
area_circle = pi * r**2
print("3. area of circle (r=5):", area_circle)

# 4. Volume v = (4/3)πr³, r = 5
volume_sphere = (4 / 3) * pi * r**3
print("4. volume of sphere (r=5):", volume_sphere)
