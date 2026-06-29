"""Week 10 exercise 3.2: find reverse pairs in words."""


if __name__ == "__main__":
    words = []
    # この.pyファイルと同じ場所にあるwords.txtを開く。
    with open(__file__.replace("10-3-2.py", "words.txt")) as f:
        for line in f:
            words.append(line.strip())

    for word in words:
        # [::-1]で文字列を後ろから読んだ形を作れる。
        revword = word[::-1]
        # word < revwordにして、同じペアを2回出さないようにしている。
        if revword in words and word < revword:
            print(word, revword)
