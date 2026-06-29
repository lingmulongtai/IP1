"""Week 11 challenge 5: count lines, words, and characters."""


if __name__ == "__main__":
    lines = 0
    words = 0
    characters = 0

    # この.pyファイルと同じ場所にあるtext2.txtを開く。
    with open(__file__.replace("11-5.py", "text2.txt")) as f:
        for line in f:
            # 1行読むたびに、行数・単語数・文字数を同時に更新する。
            lines = lines + 1
            words = words + len(line.split())
            characters = characters + len(line)

    print("lines:", lines)
    print("words:", words)
    print("characters:", characters)
