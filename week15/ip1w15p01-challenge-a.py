"""Week 15 challenge A: discover a gas law with a simulation."""

import math
import random
import turtle


width = 800
height = 600
boundary = 10


class Particle:
    """A numerical particle used for the pressure experiments."""

    def __init__(self, x, y, heading, speed):
        self.x = x
        self.y = y

        # すべての粒子を同じspeedにすると、実験で変える平均速度Vが明確になる。
        angle = math.radians(heading)
        self.dx = speed * math.cos(angle)
        self.dy = speed * math.sin(angle)

    def step(self):
        """Move once and return the momentum transferred to the walls."""

        xLimit = width / 2 - boundary
        yLimit = height / 2 - boundary
        momentumChange = 0.0

        self.x = self.x + self.dx
        if self.x < -xLimit:
            # 質量を1とすると、pxから-pxへの運動量変化の大きさは2*|px|。
            momentumChange = momentumChange + 2 * abs(self.dx)
            self.x = -2 * xLimit - self.x
            self.dx = -self.dx
        elif self.x > xLimit:
            momentumChange = momentumChange + 2 * abs(self.dx)
            self.x = 2 * xLimit - self.x
            self.dx = -self.dx

        self.y = self.y + self.dy
        if self.y < -yLimit:
            momentumChange = momentumChange + 2 * abs(self.dy)
            self.y = -2 * yLimit - self.y
            self.dy = -self.dy
        elif self.y > yLimit:
            momentumChange = momentumChange + 2 * abs(self.dy)
            self.y = 2 * yLimit - self.y
            self.dy = -self.dy

        # x = 393まで進んだ場合、右壁390を3だけ越えている。
        # 2*390-393 = 387へ鏡のように戻すことで、越えた距離を失わず反射できる。
        return momentumChange


def makeParticles(moleculeCount, speed, randomGenerator):
    particles = []
    xLimit = width / 2 - boundary
    yLimit = height / 2 - boundary

    for _ in range(moleculeCount):
        x = randomGenerator.uniform(-xLimit, xLimit)
        y = randomGenerator.uniform(-yLimit, yLimit)
        heading = randomGenerator.uniform(0, 360)
        particles.append(Particle(x, y, heading, speed))

    return particles


def estimatePressure(moleculeCount, speed, updates, seed):
    # 専用のRandomを作ると、同じseedから同じ実験結果を再現できる。
    randomGenerator = random.Random(seed)
    particles = makeParticles(moleculeCount, speed, randomGenerator)
    totalMomentum = 0.0

    for _ in range(updates):
        for particle in particles:
            totalMomentum = totalMomentum + particle.step()

    # PDFの定義どおり、壁へ渡した全運動量をworld update数で割る。
    return totalMomentum / updates


def measureConvergence(moleculeCount, speed, checkpoints, seed):
    randomGenerator = random.Random(seed)
    particles = makeParticles(moleculeCount, speed, randomGenerator)
    totalMomentum = 0.0
    results = []

    # 同じシミュレーションを続けながら測るので、update数とともに値が
    # 1つの安定した値へ近づく様子を確認できる。
    for updateNumber in range(1, max(checkpoints) + 1):
        for particle in particles:
            totalMomentum = totalMomentum + particle.step()

        if updateNumber in checkpoints:
            pressure = totalMomentum / updateNumber
            results.append((updateNumber, pressure))

    return results


def runExperiments():
    updates = 2000

    # まずNだけを変える。Vを10に固定することで、PとNの関係だけを見られる。
    fixedSpeed = 10
    numberResults = []
    for moleculeCount in range(50, 501, 50):
        pressure = estimatePressure(
            moleculeCount, fixedSpeed, updates, 1000 + moleculeCount
        )
        numberResults.append((moleculeCount, pressure))

    # 次はNを100に固定し、Vだけを5から50まで変える。
    fixedCount = 100
    speedResults = []
    for speed in range(5, 51, 5):
        pressure = estimatePressure(fixedCount, speed, updates, 2000 + speed)
        speedResults.append((speed, pressure))

    checkpoints = (100, 500, 1000, 2000, 5000)
    convergence = measureConvergence(100, 10, checkpoints, 3000)

    return convergence, numberResults, speedResults, fixedSpeed, fixedCount


def printResults(convergence, numberResults, speedResults, fixedSpeed, fixedCount):
    print("Pressure convergence (N = 100, V = 10)")
    print("updates\tP")
    for updates, pressure in convergence:
        print(updates, f"{pressure:.3f}", sep="\t")

    print("\nPressure versus molecule count (V = 10)")
    print("N\tP\tP/N")
    for moleculeCount, pressure in numberResults:
        print(moleculeCount, f"{pressure:.3f}", f"{pressure / moleculeCount:.4f}", sep="\t")

    print("\nPressure versus speed (N = 100)")
    print("V\tP\tP/V^2")
    for speed, pressure in speedResults:
        print(speed, f"{pressure:.3f}", f"{pressure / speed ** 2:.4f}", sep="\t")

    # P/(N*V^2)がどの実験でもほぼ同じなら、P = k*N*V^2と考えられる。
    constants = []
    for moleculeCount, pressure in numberResults:
        constants.append(pressure / (moleculeCount * fixedSpeed ** 2))
    for speed, pressure in speedResults:
        constants.append(pressure / (fixedCount * speed ** 2))
    k = sum(constants) / len(constants)

    # 横幅W、縦幅Hの容器では、シミュレーションから予想される比例定数は
    # 1/W + 1/Hになる。今回の実験値kがこれに近いかも確認する。
    accessibleWidth = width - 2 * boundary
    accessibleHeight = height - 2 * boundary
    theoreticalK = 1 / accessibleWidth + 1 / accessibleHeight

    # PDFのPは全壁が1 updateで受け取る運動量で、正確には全壁への力に相当する。
    # これを壁の全長で割った物理的な圧力なら、P*面積/(N*V^2)は約1/2になる。
    area = accessibleWidth * accessibleHeight
    perimeter = 2 * (accessibleWidth + accessibleHeight)
    idealGasConstant = k * area / perimeter

    print(f"\nEstimated law: P = {k:.5f} * N * V^2")
    print(f"Theoretical coefficient: 1/W + 1/H = {theoreticalK:.5f}")
    print(f"Physical pressure check: P*area/(N*V^2) = {idealGasConstant:.3f} (expected 0.5)")
    print("P is proportional to N, and proportional to V^2.")
    print(
        "Because temperature T is proportional to V^2, "
        "this agrees with P*volume proportional to N*T."
    )


def drawLine(pen, x1, y1, x2, y2):
    pen.up()
    pen.goto(x1, y1)
    pen.down()
    pen.goto(x2, y2)
    pen.up()


def drawGraph(pen, data, left, bottom, graphWidth, graphHeight, title, xLabel, color):
    xMaximum = max(x for x, _ in data)
    yMaximum = max(y for _, y in data) * 1.1

    pen.pencolor("black")
    drawLine(pen, left, bottom, left + graphWidth, bottom)
    drawLine(pen, left, bottom, left, bottom + graphHeight)

    # y軸を5分割し、値を読み取りやすくするための補助線と目盛りを書く。
    for tick in range(6):
        value = yMaximum * tick / 5
        y = bottom + graphHeight * tick / 5
        pen.pencolor("lightgray")
        drawLine(pen, left, y, left + graphWidth, y)
        pen.pencolor("black")
        pen.goto(left - 8, y - 5)
        pen.write(f"{value:.0f}", align="right", font=("Arial", 8, "normal"))

    pen.goto(left + graphWidth / 2, bottom + graphHeight + 24)
    pen.write(title, align="center", font=("Arial", 13, "bold"))
    pen.goto(left + graphWidth / 2, bottom - 42)
    pen.write(xLabel, align="center", font=("Arial", 10, "normal"))
    pen.goto(left, bottom + graphHeight + 5)
    pen.write("pressure P", align="left", font=("Arial", 9, "normal"))

    pen.pencolor(color)
    firstPoint = True
    for xValue, yValue in data:
        x = left + xValue / xMaximum * graphWidth
        y = bottom + yValue / yMaximum * graphHeight

        if firstPoint:
            pen.up()
            pen.goto(x, y)
            pen.down()
            firstPoint = False
        else:
            pen.goto(x, y)
        pen.dot(7, color)

        # 今回は各系列が10点だけなので、すべてのx値を軸の下に表示できる。
        pen.up()
        pen.goto(x, bottom - 18)
        pen.pencolor("black")
        pen.write(str(xValue), align="center", font=("Arial", 8, "normal"))
        pen.pencolor(color)
        pen.goto(x, y)
        pen.down()

    pen.up()


def plotResults(numberResults, speedResults):
    screen = turtle.Screen()
    screen.setup(1050, 650)
    screen.title("Week 15 Challenge A: gas law experiment")
    screen.tracer(0, 0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    drawGraph(
        pen, numberResults, -480, -245, 410, 440,
        "Pressure versus N", "number of molecules N", "blue"
    )
    drawGraph(
        pen, speedResults, 70, -245, 410, 440,
        "Pressure versus V", "molecule speed V", "red"
    )

    screen.update()
    screen.exitonclick()


def main():
    results = runExperiments()
    convergence, numberResults, speedResults, fixedSpeed, fixedCount = results
    printResults(convergence, numberResults, speedResults, fixedSpeed, fixedCount)
    plotResults(numberResults, speedResults)


if __name__ == "__main__":
    main()
