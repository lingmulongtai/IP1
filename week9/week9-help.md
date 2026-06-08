# Week9 コード説明（IP1x09）

`words.txt` と `text.txt` は `week9` フォルダに置いて、`week9` から実行してください。

9-1-1.py

avoids(word, letters) は、word の中に letters のどれか1文字でも含まれていたら False を返します。
全部含まれていなければ True です。
letters の各文字を for で調べ、word に ch in word で存在するか確認しています。

9-1-2.py

ユーザーに forbidden letters を input で入力してもらい、words.txt の単語のうち avoids が True になる個数を数えます。
9-1-1 の avoids をこのファイル内にも書いてあります（実行するときはこの1ファイルだけで動きます）。
例: 禁止文字 ct なら 49100 語。

9-2-1.py

uses_only(word, letters) は、word の各文字が letters の中にだけ含まれているか調べます。
letters にない文字が1つでもあれば False、全部 letters の中なら True です。

9-2-2.py

uses_only を使って、words.txt から "acefhlo" だけで書ける単語を全部 print します（188語）。

9-2-3.py

uses_all(word, letters) は、letters の各文字が word に少なくとも1回ずつ出てくるか調べます。
関数本体は return all(ch in word for ch in letters) の1行です。

9-2-4.py

uses_all を使って、words.txt の中で全部の母音 aeiou を含む単語数と、aeiouy を含む単語数を数えます。
aeiou は 598 語、aeiouy は 42 語です。

9-3-1.py

is_monotonic(word) は、左から右へ見たとき文字がアルファベット順（同じ文字の連続はOK）かどうかを返します。
隣同士を比較して、前の文字が後ろより大きければ False です。
words.txt では monotonic な単語は 596 語あります。

9-3-2.py

is_double(word, position) で position と position+1 が同じ文字か調べます。
has_triple_double で、3組の連続する二重文字（例: bookkeeper の oo, kk, ee）がある単語を探します。
index 0 から len(word)-6 まで is_double を3回（i, i+2, i+4）使って確認します。
該当するのは bookkeeper, bookkeepers, bookkeeping, bookkeepings の4語です。

9-4-1.py

words.txt の全単語の長さの平均を計算し、round(..., 1) で小数第1位まで表示します。
答えは 7.9 です。

9-4-2.py

PDF と同じ形式で、各アルファベット文字が words.txt に何回出るかを数え、* のヒストグラムを print します。
count が 0 より大きいとき count + 1000 してから count // 1000 本の * を出すので、1文字でも出れば最低1本は表示されます。
最も多い文字は e です。

9-4-3.py

単語の長さ 1〜25 について、同じやり方で * のヒストグラムを print します。
最も多い単語の長さは 8 文字です（26442 語）。

9-5-1.py

text.txt を1行ずつ読み、非文字→文字に変わった瞬間を「単語の始まり」として数えます。
ch.isalpha() で文字かどうか判定し、in_word フラグで状態を管理します。
答えは 288 語です。

9-5-2.py

9-5-1 を拡張して、行数・単語数・文字数（改行含む len(line)）を同時に数え、最後に3つまとめて print します。
答えは lines: 31, words: 288, characters: 1591 です。
