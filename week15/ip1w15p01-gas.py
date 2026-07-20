"""Week 15 project 1: simulate gas molecules with Turtle objects."""

import math
import random
import time
import turtle


# シミュレーションで使う容器の内側の大きさ。
width = 800
height = 600

# circleの標準サイズは約20ピクセルなので、中心を壁から10ピクセル離す。
# この余白がないと、中心は画面内でも円の半分が壁の外に出てしまう。
boundary = 10


# Sprite(Turtle)と書くことで、SpriteはTurtleの移動・描画機能を全部受け継ぐ。
# そこへ速度を覚える属性dx/dyと、1フレーム動かすstepを追加している。
class Sprite(turtle.Turtle):
    """A moving gas molecule drawn as a Turtle."""

    def __init__(self, x, y, heading, speed):
        # SpriteはTurtleのサブクラスなので、まずTurtle部分を初期化する。
        # これを呼ばないと、gotoやshapeなどのTurtleの機能を正しく使えない。
        turtle.Turtle.__init__(self)

        self.up()  # 移動した跡を線として描かず、分子の円だけを表示する。
        self.goto(x, y)
        self.shape("circle")

        # headingは度で与えられるが、math.cosとmath.sinはラジアンを使う。
        # 例えば0度なら(dx, dy)=(speed, 0)、90度ならほぼ(0, speed)になる。
        angle = math.radians(heading)
        self.dx = speed * math.cos(angle)
        self.dy = speed * math.sin(angle)
        # dxとdyをselfの属性にすることで、__init__が終わった後も各Spriteが
        # 自分専用の速度を覚えておき、stepを呼ぶたびに同じ速度を使える。

    def step(self):
        """Move one frame, reflecting the velocity at the four walls."""

        # position()は現在位置を(x, y)のタプルで返すので、2変数へ分けて受け取る。
        oldX, oldY = self.position()
        newX = oldX + self.dx
        newY = oldY + self.dy

        # Turtleの座標(0, 0)は画面中央。したがって左右の壁は約±width/2になる。
        # そこから円の半径boundaryを引いた値を、中心が動ける限界にする。
        xLimit = width / 2 - boundary
        yLimit = height / 2 - boundary

        # 左右の壁に当たる時は横方向の速度だけを反転する。
        # oldXから反転後の速度で計算し直すので、円が壁の外に残らない。
        if newX < -xLimit or newX > xLimit:
            self.dx = -self.dx
            newX = oldX + self.dx

        # 上下の壁では縦方向だけを反転する。角なら両方のifが実行される。
        if newY < -yLimit or newY > yLimit:
            self.dy = -self.dy
            newY = oldY + self.dy

        # 反射の計算が全部終わってから、Turtleを新しい位置へ実際に移す。
        self.goto(newX, newY)


def main():
    screen = turtle.Screen()
    # 容器の大きさに、上下左右のための少しの余白を加えてウィンドウを作る。
    screen.setup(width + 20, height + 20)

    # 自動更新を止め、100個すべてを動かした後に一度だけ描き直す。
    # 1個動かすたびに描画するよりも、アニメーションがかなり滑らかになる。
    screen.tracer(0, 0)

    # 作ったSpriteをリストへ残しておけば、後のループで全員にstepを命令できる。
    sprites = []
    for _ in range(100):
        # _は、100回という回数だけが必要でループ番号は使わないという意味。
        # 最初から壁と重ならないように、boundaryの分だけ内側で作る。
        x = random.randint(-width // 2 + boundary, width // 2 - boundary)
        y = random.randint(-height // 2 + boundary, height // 2 - boundary)
        # 0～359度で全方向を選び、速さもPDFの例にある3～7から選ぶ。
        # 分子ごとに値が違うので、全員が同じ向きに並んで動くことを避けられる。
        heading = random.randint(0, 359)
        speed = random.randint(3, 7)
        sprites.append(Sprite(x, y, heading, speed))

    try:
        # while Trueには終了条件がないため、ウィンドウを閉じるまで動き続ける。
        while True:
            # リストに保存した全分子を1回ずつ進めると、1フレームが完成する。
            for sprite in sprites:
                sprite.step()

            screen.update()
            time.sleep(0.04)  # 約25フレーム/秒にして、速すぎる動きを抑える。
    except turtle.Terminator:
        # ウィンドウを閉じた時にTurtleの終了例外を画面へ表示させない。
        pass


if __name__ == "__main__":
    # importしてテストする時には動かさず、直接実行した時だけ無限ループを始める。
    main()
