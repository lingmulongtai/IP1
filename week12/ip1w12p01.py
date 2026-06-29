"""Week 12 project 1: print 20 random words from text3.txt."""

from pathlib import Path
import random


def fileWords(fileName):
    allWords = []
    with open(fileName, encoding="utf-8") as file:
        for line in file:
            words = line.split()
            allWords.extend(words)
    return allWords


words = fileWords(Path(__file__).with_name("text3.txt"))

for _ in range(20):
    word = random.choice(words)
    print(word)
