"""Week 12 project 2: generate a sentence using a Markov model."""

from pathlib import Path
import random


prefixlen = 2


def fileWords(fileName):
    allWords = []
    with open(fileName, encoding="utf-8") as file:
        for line in file:
            words = line.split()
            allWords.extend(words)
    return allWords


def buildMarkov(words, prefixlen):
    markov = {}
    for i in range(len(words) - prefixlen):
        prefix = tuple(words[i:i + prefixlen])
        suffix = words[i + prefixlen]
        markov[prefix] = markov.get(prefix, []) + [suffix]
    return markov


def startsWithCapital(prefix):
    first = prefix[0]
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

            suffix = random.choice(suffixes)
            result.append(suffix)

            if suffix.endswith("."):
                return " ".join(result)

            prefix = prefix[1:] + (suffix,)


words = fileWords(Path(__file__).with_name("text3.txt"))
markov = buildMarkov(words, prefixlen)
print(makeSentence(markov))
