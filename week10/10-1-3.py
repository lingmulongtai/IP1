"""Week 10 exercise 1.3: nested_sum(n)."""


def nested_sum(n):
    # 整数そのものなら、それ以上分解せずにその値を返す。
    if type(n) is int:
        return n
    elif type(n) is list:
        # リストなら中身を一つずつ同じ関数に任せる。深さは気にしなくてよい。
        result = 0
        for item in n:
            result = result + nested_sum(item)
        return result
    else:
        # Noneや文字列など、整数でもリストでもないものは合計に入れない。
        return 0


if __name__ == "__main__":
    print(nested_sum([None, 1, [2, "two", [[[[3, False, 4]]]], []], 5]))


# Falseはbool型なので、type(False) is int にはならず、足されない。
