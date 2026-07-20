"""Week 14 project 3: sort random lists with selection sort."""

import random


def ranlist(n):
    """Return a list containing n random integers from 0 through n."""

    # 空のリストへ1個ずつappendし、最後にn個入りのリストとして返す。
    numbers = []
    for _ in range(n):
        # _は繰り返し回数の値を使わないという意味。
        # randintは両端を含むので、この値は0以上n以下になる。
        numbers.append(random.randint(0, n))
    return numbers


def selectionSort(numbers):
    """Sort numbers in place using the selection sort algorithm."""

    length = len(numbers)

    # iより左側は、すでに小さい順で正しい位置に確定している。
    # 最後の1個は残った時点で自動的に正しいため、length-1回で十分。
    for i in range(length - 1):
        # この1周が終わると、位置iにも残りの中の最小値が確定する。
        # 未整列部分の先頭を、ひとまず最小値の位置だと考える。
        # 値そのものではなく位置を覚えるのは、後で交換するため。
        mindex = i

        # iより前はもう完成しているので、i+1から末尾だけを調べる。
        for j in range(i + 1, length):
            if numbers[j] < numbers[mindex]:
                mindex = j

        # 未整列部分で見つけた最小値を位置iへ移す。
        # タプル代入なら一時変数を作らず、2要素を同時に交換できる。
        # mindexがiと同じ場合も、同じ要素同士を交換するだけなので問題ない。
        numbers[i], numbers[mindex] = numbers[mindex], numbers[i]

    # 新しいリストを返さず、引数として受け取った同じリストを直接変更する。
    # これがPDFに書かれているin-place（インプレース）の整列。


# PDF本文はselsort、配布疑似コードとテスト例はselectionSortという名前なので、
# どちらを使っても同じ関数が呼ばれるように別名を用意する。
# 新しい処理をコピーするのではなく、同じ関数オブジェクトへ2つの名前を付ける。
selsort = selectionSort


if __name__ == "__main__":
    for _ in range(20):
        values = ranlist(10)
        print(values, end="\t")
        selectionSort(values)
        print(values)

        # Python標準のsortedが作る答えと比べ、違えばその場で停止する。
        # assertの条件がFalseならAssertionErrorになり、間違いを見逃さない。
        # 20回すべて通れば、画面には整列前と整列後の20組が表示される。
        assert values == sorted(values)
