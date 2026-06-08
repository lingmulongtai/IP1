"""Week 7 exercise 4: Newton's method for square roots."""


def newton(n, epsilon=0.0000001):
    s = n / 2

    while abs(s * s - n) >= epsilon:
        s = (s + n / s) / 2

    return s


if __name__ == "__main__":
    print("--- 4.1: newton(100) ---")
    print(newton(100))

    print("--- 4.2-4.4: newton(n, epsilon) ---")
    for n in [1, 2, 10, 100]:
        print(n, newton(n, 0.00001))

    print("--- 4.3: different epsilon on n=2 ---")
    for eps in [0.1, 0.001, 0.00001]:
        print("epsilon", eps, "->", newton(2, eps))

    print("--- 4.4: one part in ten million ---")
    for n in [1, 2, 10, 100]:
        print(n, newton(n, 0.0000001))