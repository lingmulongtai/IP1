"""Week 4 exercise 1: mathematical functions."""

import math

def circle_area(r):
    return math.pi * r**2

def sphere_volume(r):
    return (4 / 3) * math.pi * r**3

def triangle_area(a, b):
    return (a * b) / 2

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def point_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

for r in [1, 2, 3]:
    print("circle_area(", r, ") =", circle_area(r))

for r in [1, 2, 3]:
    print("sphere_volume(", r, ") =", sphere_volume(r))

print("triangle_area(1, 1) =", triangle_area(1, 1))
print("triangle_area(2, 2) =", triangle_area(2, 2))
print("triangle_area(3, 4) =", triangle_area(3, 4))

print("hypotenuse(1, 1) =", hypotenuse(1, 1))
print("hypotenuse(3, 4) =", hypotenuse(3, 4))
print("hypotenuse(5, 12) =", hypotenuse(5, 12))

print("point_distance(0, 0, 1, 1) =", point_distance(0, 0, 1, 1))
print("point_distance(3, 4, 6, 8) =", point_distance(3, 4, 6, 8))
print("point_distance(8, 6, 4, 3) =", point_distance(8, 6, 4, 3))
