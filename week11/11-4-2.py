"""Week 11 exercise 4.2: remove punctuation from text."""


def isLetter(c):
    # 句読点は落としたいが、単語の間の空白は残しておく。
    return c.isalpha() or c.isspace()


def depunctuate(word):
    # filterで残したい文字だけ通し、joinで文字列に戻す。
    return "".join(filter(isLetter, word))


if __name__ == "__main__":
    # この.pyファイルと同じ場所にあるtext2.txtを開く。
    with open(__file__.replace("11-4-2.py", "text2.txt")) as f:
        for line in f:
            print(depunctuate(line), end="")
