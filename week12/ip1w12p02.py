"""Week 12 project 2: generate a sentence using a Markov model."""

import random


prefixlen = 2


def fileWords(fileName):
    allWords = []
    with open(fileName, encoding="utf-8") as file:
        for line in file:
            # まず本文全体を、単語が順番に並んだ1つのリストにする。
            words = line.split()
            allWords.extend(words)
    return allWords


def buildMarkov(words, prefixlen):
    markov = {}
    for i in range(len(words) - prefixlen):
        # prefixlen個の単語をキーにして、その直後に来た単語を候補として覚える。
        prefix = tuple(words[i:i + prefixlen])
        suffix = words[i + prefixlen]
        markov[prefix] = markov.get(prefix, []) + [suffix]
    return markov


def startsWithCapital(prefix):
    first = prefix[0]
    # ボーナス用。文の始まりらしく、大文字で始まるprefixだけ使う。
    return len(first) > 0 and first[0].isupper()


def randomCapitalPrefix(markov):
    while True:
        prefix = random.choice(list(markov.keys()))
        if startsWithCapital(prefix):
            return prefix


def makeSentence(markov):
    while True:
        prefix = randomCapitalPrefix(markov)
        result = list(prefix)

        if result[-1].endswith("."):
            return " ".join(result)

        for _ in range(200):
            suffixes = markov.get(prefix)
            if suffixes is None:
                break

            # 今のprefixに続けられる単語の中から1つ選ぶ。
            suffix = random.choice(suffixes)
            result.append(suffix)

            # ピリオドで終わる単語が出たら、そこで文を終わらせる。
            if suffix.endswith("."):
                return " ".join(result)

            # 古い先頭の単語を落として、新しい単語を後ろに足す。
            prefix = prefix[1:] + (suffix,)


# この.pyファイルと同じ場所にあるtext3.txtを読む。
words = fileWords(__file__.replace("ip1w12p02.py", "text3.txt"))
markov = buildMarkov(words, prefixlen)
print(makeSentence(markov))
