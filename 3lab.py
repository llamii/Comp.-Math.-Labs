import math
from matform import *
a, b = 0.4, 0.9
h = (b - a) / 10


def func(x):  # функция
    return x ** 2 + math.log(x)


tableX = [int((a + i * h) * 100) / 100 for i in range(11)]  # узлы
tableY = [func(tableX[i]) for i in range(11)]  # функции в узлах

tableLeft = [tableY[i + 1] - tableY[i] for i in range(10)]  # конечные разности для левых
tableRight = [tableY[i] - tableY[i - 1] for i in range(10, 0, -1)]  # конечные разности для правых
tableCenter = []  # конечные разности для центральных
for i in range(int((len(tableY) - 1) / 2)):  # заполнение
    centerIndex = int((len(tableY) - 1) / 2)
    tableCenter.append(tableY[centerIndex] - tableY[centerIndex - i - 1])
    tableCenter.append(tableY[centerIndex + i + 1] - tableY[centerIndex])


def tNewton1(xStar):
    return (xStar - a) / h


def tNewton2(xStar):
    return (xStar - b) / h


def tGauss2(xStar):
    center = ((b - a) / 2) + a
    return (xStar - center) / h


def Omega(xStar):
    result = 1
    for i in range(11):
        if (tableX[i] < xStar):
            result *= (xStar - tableX[i])
    return result


def R(value, xStar):
    return func(value) * Omega(xStar) / 39916800.0


def Newton1(xStar):
    result = tableY[0]
    t = tNewton1(xStar)
    tRep = t
    n = 1
    for i in range(int(len(tableLeft))):
        n *= (i + 1)
        result += (tRep * tableLeft[i] / n)
        tRep *= (t - i)
    return result


def Newton2(xStar):
    result = tableY[10]
    t = tNewton2(xStar)
    tRep = t
    n = 1
    for i in range(int(len(tableRight)) - 1, -1, -1):
        n *= (len(tableRight) - i + 1)
        result += (tRep * tableRight[i] / n)
        tRep *= (t + (int(len(tableRight)) - i))
    return result


def Gauss2(xStar):  # t_0 + right_1 + t_0(2) + left_1 ...
    centerFunc = tableY[int(len(tableY) - 1 / 2)]
    result = centerFunc
    t = tGauss2(xStar)
    tRep = t
    n = 1
    sign = True
    j = 0
    for i in range(20):
        n *= (i + 1)
        if i % 2 == 0:
            result += tRep * centerFunc / n
        else:
            result += tRep * tableCenter[j] / n
            if sign:
                tRep *= (t + i + 1)
                sign = False
            else:
                tRep *= (t - i - 1)
                sing = True
            j += 1
    return result


def Task(xStar, L):
    minR = R(b, xStar)
    maxR = R(a, xStar)
    # print(minR, "<", L - func(xStar), "<", maxR)
    print("True") if minR < L - func(xStar) < maxR else print("False")


print("1")
xStar2 = 0.43
Tаsk(xStar2, Newton1(xStar2))
print("2")
xStar3 = 0.86
Tаsk(xStar3, Newton2(xStar3))
print("3")
xStar4 = 0.67
Tаsk(xStar4, Gauss2(xStar4))
