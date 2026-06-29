"""Week 12 project 1: print 20 random words from text3.txt."""

import random


def fileWords(fileName):
    allWords = []
    with open(fileName, encoding="utf-8") as file:
        for line in file:
            # splitで1行を単語に分けて、全部同じリストに足していく。
            words = line.split()
            allWords.extend(words)
    return allWords


# この.pyファイルと同じ場所にあるtext3.txtを読む。
words = fileWords(__file__.replace("ip1w12p01.py", "text3.txt"))

for _ in range(20):
    # リストから1語だけランダムに選んで、そのまま表示する。
    word = random.choice(words)
    print(word)
