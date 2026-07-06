"""Week 13 project 3: plot a function entered by the user."""

from math import *
from turtle import *


def evaluateExpression(expression):
    return float(eval(expression))


def evaluateFunction(functionText, x):
    return float(eval(functionText))


def plotFunction(functionText, xminText, xmaxText):
    try:
        xmin = evaluateExpression(xminText)
        xmax = evaluateExpression(xmaxText)
        if xmin == xmax:
            print("The minimum and maximum cannot be the same.")
            return

        xscale = (xmax - xmin) / 400
        points = []
        for wx in range(401):
            # wxは画面上の横位置、xは関数に入れる実際の値。
            x = xmin + wx * xscale
            y = evaluateFunction(functionText, x)
            points.append((wx, y))
    except Exception as e:
        print("I could not evaluate that expression:", e)
        return

    ymin = points[0][1]
    ymax = ymin
    for wx, y in points:
        ymin = min(ymin, y)
        ymax = max(ymax, y)

    if ymin == ymax:
        # 横一直線の関数でも、縦の縮尺が0にならないようにする。
        ymin = ymin - 1
        ymax = ymax + 1

    yscale = 400 / (ymax - ymin)

    setup(500, 500)
    reset()
    speed(0)
    up()

    for wx, y in points:
        # 関数の値を、中央寄せの400ピクセル四方に変換して描く。
        wy = (y - ymin) * yscale
        goto(-200 + wx, -200 + wy)
        down()

    up()
    goto(0, 0)
    mainloop()


def printMenu(functionText, xminText, xmaxText):
    print("1) change function:", functionText)
    print("2) change minimum:", xminText)
    print("3) change maximum:", xmaxText)
    print("4) plot function")
    print("5) exit")


if __name__ == "__main__":
    functionText = "sin(x)"
    xminText = "-2*pi"
    xmaxText = "2*pi"

    while True:
        printMenu(functionText, xminText, xmaxText)
        choice = input("choice: ").lower().strip()

        if choice == "1" or choice == "function":
            functionText = input("new function: ")
        elif choice == "2" or choice == "minimum":
            xminText = input("new minimum: ")
        elif choice == "3" or choice == "maximum":
            xmaxText = input("new maximum: ")
        elif choice == "4" or choice == "plot":
            plotFunction(functionText, xminText, xmaxText)
        elif choice == "5" or choice == "exit":
            break
        else:
            print("Please choose 1, 2, 3, 4, or 5.")
