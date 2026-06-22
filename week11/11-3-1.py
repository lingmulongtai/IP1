"""Week 11 exercise 3.1: memoise Fibonacci results and measure speed."""

import time


def fib_without_memo(n):
    if n < 2:
        return 1
    return fib_without_memo(n - 1) + fib_without_memo(n - 2)


memo = dict()


def fib(n):
    if n in memo:
        return memo[n]
    if n < 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result


if __name__ == "__main__":
    n = 32

    start = time.perf_counter()
    slow_result = fib_without_memo(n)
    slow_time = time.perf_counter() - start

    memo.clear()
    start = time.perf_counter()
    fast_result = fib(n)
    fast_time = time.perf_counter() - start

    print("fib(", n, ") = ", fast_result, sep="")
    print("without memo:", slow_time, "seconds")
    print("with memo:", fast_time, "seconds")
    print("times faster:", slow_time / fast_time)
    print("same result:", slow_result == fast_result)
