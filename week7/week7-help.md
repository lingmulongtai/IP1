# Week7 コード説明（IP1x07）

7-1

Pythonの三角関数はradianを使うので、degreeを受け取れるwrapper functionを作りました。
math.radians(x)でdegreeからradianに変換してから、math.sin, math.cos, math.tanを呼び出しています。

7-2-1

factorial(n)の再帰の動きを確認するために、関数が呼ばれるたびにfactorial nを表示し、returnの直前にreturning resultを表示しています。
factorial(5)では、5から0まで呼び出され、その後戻りながら計算されて120になります。

7-2-2

階乗は0以上の整数だけを対象にするので、最初に引数チェックを追加しました。
整数でない場合はargument must be an integer、負の数の場合はargument must be non-negativeと表示して、Noneを返します。

7-2-3

2.2では再帰のたびに引数チェックをしていましたが、ここでは最初の1回だけチェックするようにしました。
外側のfactorial(n)でチェックし、正しい値なら内部用の_factorial(n)で再帰計算をします。

7-3-1

while Trueで入力を繰り返し、入力がstopならbreakで終了します。
それ以外の場合は、入力を整数に変換して2倍した値を表示します。

7-3-2

totalで合計、countで入力された整数の個数を管理しています。
数値が入力されるたびに合計と個数を更新し、平均をtotal / countで計算しています。
stopが入力されたら計算せずに終了します。

7-4

Newton's methodを使って平方根を近似しています。
最初にs = n / 2を予想値にして、誤差abs(s * s - n)が十分小さくなるまで、s = (s + n / s) / 2で更新します。
n * epsilonを使っているので、relative accuracyになっています。

7-5

自分で作ったnewton()の結果と、Pythonのmath.sqrt()の結果を比較する表を作りました。
for n in range(1, 10)で1から9まで計算し、それぞれの差をabs(approx - exact)で求めています。
pad()は表の列をそろえるための関数です。