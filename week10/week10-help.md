# Week10 コード説明（IP1x10）

`words.txt` は `week10` フォルダに置いて、`week10` から実行してください。

10-1-1.py

total(numbers) はリスト内の数値をすべて足して返します。
for で各要素を result に加算しています。

10-1-2.py

cumulative(numbers) は累積和のリストを返します。
running に足しながら result に append していきます。

10-1-3.py

nested_sum(n) はネストしたリストの中の整数だけを再帰的に足します。
type(n) is int ならその値を、type(n) is list なら各要素を再帰、それ以外は 0 を返します。
例: nested_sum([None, 1, [2, "two", [[[[3, False, 4]]]], []], 5]) → 15

10-1-4.py

is_ordered(things) は要素が昇順（<=）かどうかを返します。
隣同士を比較し、前が後より大きければ False です。

10-1-5.py

is_anagram(a, b) は sorted(a) == sorted(b) でアナグラムか判定します。

10-2-1.py

randlist(n, i, j) は random.randint を使い、i〜j の乱数を n 個入れたリストを返します。

10-2-2.py

has_duplicates(l) はリストに重複があるか返します。
sorted して隣接要素が同じかどうかを調べます（PDF のヒント通り）。

10-2-3.py

誕生日のパラドックスをシミュレーションします。
100,000 回試行して、n 人のうち同じ誕生日がいる割合を計算します。
答え: 50% は約 23 人（最小 n は 23 前後）、90% は約 41 人。

10-3-1.py

words.txt を読み込み、各行を strip() して words リストに入れます。
単語数は 113783 語です。

10-3-2.py

words の各単語について逆順 revword を作り、words に含まれていれば reverse pair として表示します。
word < revword で重複表示を避けます（pool/loop のようなペア）。

10-3-3.py

includes(sequence, target) で二分探索を実装し、10-3-2 を高速化した版です。
words がソート済みなので O(log n) で検索できます。結果は 10-3-2 と同じですがかなり速いです。

10-4-1.py

interlocking（交互に文字を取る）単語ペアを探します。
6文字以上の単語を word[0::2] と word[1::2] に分割し、両方が words にあればペアです。
includes で二分探索します。答えは 561 ペアです。

10-4-2.py

3-way interlocking を探します。
9文字以上の単語を word[0::3], word[1::3], word[2::3] に分割し、3つとも words にあれば triple です。
答えは 178 組です。
