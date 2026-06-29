"""Week 10 exercise 3.1: read words.txt into a list."""


if __name__ == "__main__":
    words = []
    # この.pyファイルと同じ場所にあるwords.txtを開く。
    with open(__file__.replace("10-3-1.py", "words.txt")) as f:
        for line in f:
            # stripしないと単語の最後に改行が残って検索しにくい。
            words.append(line.strip())

    print("words loaded:", len(words))
    print("first word:", words[0])
    print("last word:", words[-1])
