"""Week 3 exercise 2: Celsius ↔ Fahrenheit (algorithm order + implementation)."""

# --- Part 1: Celsius → Fahrenheit (f = (9/5)*c + 32, i.e. c*1.8 + 32) ---
c = int(input("c: "))
f = c * 1.8
f = f + 32
print(f)

print()

# --- Part 2: Fahrenheit → Celsius (c = (5/9)*(f - 32)) ---
f_in = int(input("f: "))
c_out = f_in - 32
c_out = c_out * 5
c_out = c_out / 9
print(c_out)
