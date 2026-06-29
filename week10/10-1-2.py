"""Week 10 exercise 1.2: cumulative(numbers)."""


def cumulative(numbers):
    result = []
    # runningには「ここまでの合計」を入れておく。
    running = 0
    for n in numbers:
        running = running + n
        # 合計が更新されるたびに、その時点の値を答えのリストへ残す。
        result.append(running)
    return result


if __name__ == "__main__":
    print(cumulative([]))               # []
    print(cumulative([1]))              # [1]
    print(cumulative([1, 2, 3, 4, 5]))  # [1, 3, 6, 10, 15]
    print(cumulative(range(10)))        # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
