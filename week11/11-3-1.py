"""Week 11 exercise 3.1: memoise Fibonacci results and measure speed."""

import time


def fib_without_memo(n):
    if n < 2:
        return 1
    return fib_without_memo(n - 1) + fib_without_memo(n - 2)


# 一度計算したfib(n)をここに保存して、同じ計算を繰り返さない。
memo = dict()


def fib(n):
    if n in memo:
        return memo[n]

    if n < 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)

    # 初めて出たnだけ計算し、その答えを次回用に覚えておく。
    memo[n] = result
    return result


if __name__ == "__main__":
    n = 32

    # まず普通の再帰版を測って、比較用の時間を作る。
    start = time.time()
    slow_result = fib_without_memo(n)
    slow_time = time.time() - start

    memo.clear()
    start = time.time()
    fast_result = fib(n)
    fast_time = time.time() - start

    print("fib(", n, ") = ", fast_result, sep="")
    print("without memo:", slow_time, "seconds")
    print("with memo:", fast_time, "seconds")
    print("times faster:", slow_time / fast_time)
    print("same result:", slow_result == fast_result)
