# Week8 コード説明（IP1x08）

各 `.py` は課題 PDF の節に対応しています。

## `8-1.py` while ループ（4点）

| 関数 | 内容 |
|------|------|
| **print_each(n)** | `i` を 0 から増やし、`i < n` の間 `print(i)`。0〜n−1。 |
| **print_each1(x)** | `len(x)` まで `x[i]` を1行ずつ表示。 |
| **print_each2(x, n)** | インデックス `n` から末尾まで表示。`print_each2("goodbye", 4)` → b,y,e。 |
| **print_each3(x, n=0)** | `n` を省略すると先頭から全体（デフォルト引数）。 |

## `8-2.py` シーケンス内の要素（4点）

| 関数 | 内容 |
|------|------|
| **find_letter** | `while` で最初の一致インデックス。なければ `None`。 |
| **find_letter1** | 同じ処理を `for i in range(len(word))` で実装。 |
| **count_letter** | 1文字の出現回数。 |
| **count_letters** | 外側 `for ch in letters`、内側で `word` を走査する二重ループ。複数文字の合計回数。 |

## `8-3.py` 回文（2点）

- **palindrome(string)**: 先頭と末尾を `string[i]` と `string[length-1-i]` で比較。
- **palindrome1(s)**: 1行 `return s == s[::-1]`（スライスで反転比較）。

## `8-4.py` チャレンジ rotate（ボーナス1点）

- **`rotate(string, n)`**: 小文字・大文字それぞれ `a`/`A` 基準で `(ord(c) - ord('a') + n) % 26` し `chr` で戻す。それ以外はそのまま。
- `rotate(rotate(s, n), -n)` で元に戻る。
- **rot13**: 26 文字の半分だけ回すと、もう一度 rot13 すると元の文字になる（自己逆写）。だからエンコードとデコードに同じ関数が使える。

## 先生チェック用の一言

- **8-1**: 「while で 0..n−1、インデックス走査、部分列、デフォルト引数まで4段階。」
- **8-2**: 「find は while/for、count は for、複数文字は入れ子の for。」
- **8-3**: 「前後比較のループ版と `s[::-1]` の1行版。」
- **8-4**: 「アルファベットだけ `% 26` で回転。大文字小文字別。rot13 は26の半分。」
