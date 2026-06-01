"""Week 8 exercise 1: while loops and conditionals."""


def print_each(n):
    i = 0
    while i < n:
        print(i)
        i = i + 1


def print_each1(x):
    i = 0
    while i < len(x):
        print(x[i])
        i = i + 1


def print_each2(x, n):
    i = n
    while i < len(x):
        print(x[i])
        i = i + 1


def print_each3(x, n=0):
    i = n
    while i < len(x):
        print(x[i])
        i = i + 1


if __name__ == "__main__":
    print("--- 1.1 print_each(10): 0..9 ---")
    print_each(10)

    print("--- 1.2 print_each1('hello'): one letter per line ---")
    print_each1("hello")

    print("--- 1.3 print_each2('goodbye', 4): bye ---")
    print_each2("goodbye", 4)

    print("--- 1.4 print_each3('goodbye', 4) and print_each3('goodbye') ---")
    print_each3("goodbye", 4)
    print_each3("goodbye")
