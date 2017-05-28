from math import pi, sqrt, exp, sin
from assignment1 import PolynomialIntegrate
import sys


def f(x):
    return (1.0 / sqrt(2.0 * pi)) * exp((-1.0 / 2) * x ** 2.0)  # A entre 0 e 1 = 0.34134474606; de 0 a 5 = 0.49999971334
    # return exp(-(x**2))                                    #A, de 0 a 1 = 0.746824
    # return x**9+45*x**8+97*x**7+56*x                       #A, de 0 a 1: 45.225...
    # return sin(x)                                          #A, de 0 a 1 = 0.999.....


N = input("Digite a quantidade de pontos de integracao (entre 1 e 10): ")

I1 = PolynomialIntegrate(f, 0, 1.0, N)
I2 = PolynomialIntegrate(f, 0, 5.0, N)
print "\nI1 =", I1, "\n"
print "I2 =", I2

raw_input()
