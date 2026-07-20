"""Week 12 project 2: generate a sentence using a Markov model."""

import random


prefixlen = 2 #次の単語を予測するために、直前の何単語を見るか。


def fileWords(fileName):
    allWords = []
    with open(fileName, encoding="utf-8") as file:
        for line in file:
            # text3.txt の文章を読み、すべての単語を1つのリストにする。
            words = line.split() #1行を空白で分割して、単語のリストにする。文の終わりを判断するため、ピリオドも単語の一部として残す。
            allWords.extend(words) #その行の単語を、全体の単語リストの後ろに追加する。appendを使うとリストの中にリストが入ってしまうので、extendを使うことで１つの平らなリストにする。
    return allWords


def buildMarkov(words, prefixlen):
    markov = {} #空の辞書
    for i in range(len(words) - prefixlen): #単語リストを先頭から順番に調べる。prefixlen=2なら、現在位置から２単語をprefix、その次の１単語をsuffixとして取得する。
        #最後までループすると、リストの外側にある存在しない単語を取ろうとしてエラーになるので、prefixlen個分だけ手前でループを止めている。
        # prefixlen個の単語をキーにして、その直後に来た単語を候補として覚える。
        prefix = tuple(words[i:i + prefixlen]) #タプルにする。なぜなら、辞書のキーには変更可能なリストを使えないから。markov[['humpty', 'dumpty']]これはだめ。markov[('humpty', 'dumpty')]これなら辞書のキーとして使える。
        suffix = words[i + prefixlen] #suffixを取得する。prefixの直後にある単語を取り出す。
        markov[prefix] = markov.get(prefix, []) + [suffix] #辞書に追加する。そのprefixに対応するリストを取得して、suffixを後ろに追加する。
    return markov
# ('humpty', 'dumpty'): ['sat', 'had'],

def startsWithCapital(prefix): #ボーナス用。大文字で始まる場所を探す。
    first = prefix[0]
    return len(first) > 0 and first[0].isupper() 
#最初が大文字ならTrue、小文字ならFalseを返す。isupper()は文字列の最初の文字が大文字かどうかを判定する。
#len(first) > 0は、空文字列を避けるため。空文字列に対してisupper()を呼ぶとエラーになるので、まず長さが0より大きいかを確認する。

def randomCapitalPrefix(markov): #大文字のprefiをランダムに選ぶ。大文字で始まるprefixが見つかるまでループする。
    while True:
        prefix = random.choice(list(markov.keys())) #辞書に登録されているすべてのprefixをリストにする。そこからランダムに1つ選ぶ。
        if startsWithCapital(prefix):
            return prefix


def makeSentence(markov): #実際に文章を作る。
    while True:
        prefix = randomCapitalPrefix(markov) #大文字で始まるprefixをランダムに選ぶ。
        result = list(prefix) #それを生成結果のリストにｓる。prefixは辞書検索に使うためタプルのままにする。resultは後ろに単語を追加するためリストにしている。

        if result[-1].endswith("."):
            return " ".join(result)
        #最初のprefixがすでにピリオドで終わる場合は、その時点で完成。

        for _ in range(200): #最大200単語まで続ける。ここで_はループ回数の値自体は使わない。という意味。
            suffixes = markov.get(prefix) #現在のprefixに続けられる単語リストを取得する。
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
