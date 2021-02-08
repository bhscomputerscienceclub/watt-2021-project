import random


def randomNum3():
    z = random.randint(-20, 20)
    return z


def noZeros(m):
    if m == 0:
        m += 1
    return m


# Linear Generators - All return in y-inter, x-inter, and equation format. #1 doesn't have y-inter


def lineargen1():
    m, b = randomNum3(), randomNum3()
    m = noZeros(m)
    LinearEquation = "y = {}x + {}"
    printedEquation = LinearEquation.format(m, b)

    # Answer #
    xInter = round(-b / m, 2)
    yInter = round(b, 2)
    return xInter, yInter, printedEquation


def lineargen2():
    y1, m, x1 = randomNum3(), randomNum3(), randomNum3()
    m = noZeros(m)
    LinearEquation = "(y - {}) = {}(x - {})"
    printedEquation = LinearEquation.format(y1, m, x1)

    # Answer #
    yInter = round((-x1 * m) + y1, 2)
    xInter = round((-y1 + m * x1) / m, 2)

    return xInter, yInter, printedEquation


def lineargen3():
    A, B, C = randomNum3(), randomNum3(), randomNum3()
    A, B = noZeros(A), noZeros(B)
    LinearEquation = "{}x + {}y = {}"
    printedEquation = LinearEquation.format(A, B, C)

    # Answer #
    yInter = round(C / B, 2)
    xInter = round(C / A, 2)

    return xInter, yInter, printedEquation


# Random linear gen


def linearPicker():
    t = random.randint(1, 3)
    if t == 1:
        return lineargen1()
    elif t == 2:
        return lineargen2()
    else:
        return lineargen3()
