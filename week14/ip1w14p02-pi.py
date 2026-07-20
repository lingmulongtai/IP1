"""Week 14 project 2: estimate pi with a Monte Carlo simulation."""

import random
import turtle


# PDFでは最初に1000回で試し、値が安定するよう回数を増やすように書かれている。
# 計算は100万回行うが、描画は約1000点だけにして実行速度を保つ。
count = 1_000_000


def estimatePi(count, pen=None, screen=None):
    """Run count trials and return the resulting estimate of pi."""

    # 正方形へランダムな点を大量に投げ、円内へ入った割合からpiを求める。
    # このように乱数による多数の実験で数値を推定する方法がMonte Carlo法。
    if count <= 0:
        raise ValueError("count must be positive")

    # countが大きくても約1000点だけ描くための間隔。
    # maxを使うのは、countが1000未満の時にeveryが0になるのを防ぐため。
    every = max(count // 1000, 1)
    # numberOfDotsは描く予定の総数、dotsDrawnはすでに描いた数。
    # 計算する100万点すべてを描かないため、別々の変数として管理する。
    numberOfDots = min(count, 1000)
    dotsDrawn = 0
    hits = 0

    for n in range(count):
        # random()の範囲0以上1未満を、2倍して1を引くと-1以上1未満になる。
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1

        # 原点からの距離が1未満なら単位円の内側。
        # sqrtを計算しなくても、距離の2乗x*x+y*yを1と比べれば判定できる。
        inside = x * x + y * y < 1.0
        if inside:
            hits = hits + 1

        # penを渡さない場合は計算だけを行えるので、テストにも利用できる。
        if pen is not None and n % every == 0 and dotsDrawn < numberOfDots:
            # 数学上の座標[-1, 1]を、画面上の[-200, 200]へ拡大する。
            pen.goto(x * 200, y * 200)
            # 条件式を使い、円内ならblack、円外ならredを1行で選んでいる。
            pen.dot(10, "black" if inside else "red")

            # 試行の進み具合を、画面下部の-200から200までの緑色の棒で示す。
            if numberOfDots == 1:
                progressX = 200
            else:
                # dotsDrawnの0～999を、画面座標の-200～200へ変換する。
                progressX = -200 + 400 * dotsDrawn / (numberOfDots - 1)
            pen.goto(progressX, -225)
            pen.dot(5, "green")

            # tracerで自動描画を止めているため、必要な時だけ手動で更新する。
            screen.update()
            dotsDrawn = dotsDrawn + 1

    # 正方形の面積は4、単位円の面積はpiなので、内側の割合は約pi/4。
    # したがって、実験で得たhits/countを4倍するとpiを推定できる。
    return 4 * hits / count


def main():
    screen = turtle.Screen()
    # 500四方の窓を作り、自動更新を止めて描画待ち時間を減らす。
    screen.setup(500, 500)
    screen.tracer(0, 0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.up()  # 点と点の間に線を引かず、dotだけを残す。

    # 描画に使うpenとscreenを渡し、計算結果だけを戻り値で受け取る。
    estimate = estimatePi(count, pen, screen)
    print("Pi is", estimate)

    # 結果を確認できるよう、クリックされるまでウィンドウを残す。
    screen.exitonclick()


if __name__ == "__main__":
    main()
