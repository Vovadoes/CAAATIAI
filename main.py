import math

# from Charts import *

# from scipy.stats import t

# CONST
# None

class Calculation:
    def __init__(self, P, i, n, h):
        self.P = P
        self.i = i
        self.n = n
        self.h = h
        self.C = None

    def f1(self):
        self.C = self.P * (1 + self.i * self.n / 100) / (math.pow(1 + self.h / 100, self.n))

    def f2(self):
        self.C = self.P * pow(1 + self.i / 100, self.n) / (math.pow(1 + self.h / 100, self.n))


if __name__ == "__main__":
    P = 100
    i = 20
    n = 2
    h = 8

    calculation = Calculation(P, i, n, h)
    calculation.f1()
    print(calculation.C)
    calculation.f2()
    print(calculation.C)

    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
