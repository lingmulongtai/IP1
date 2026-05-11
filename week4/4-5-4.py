"""Week 4 challenge 5.4: generalize twice() with *args."""


def twice(f, *args):
    f(*args)
    f(*args)


twice(twice, twice, print, "cool!")

# Prediction requested in the worksheet:
print("Prediction for twice(twice, twice, print, 'cooler!'):")
print("It prints 'cooler!' 8 times.")
