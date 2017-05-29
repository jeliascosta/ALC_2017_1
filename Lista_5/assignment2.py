from math import pi, sqrt, exp, sin, cos
from assignment1 import PolynomialIntegration, GaussianIntegration


def f(x):
    return (1.0 / sqrt(2.0 * pi)) * exp((-1.0 / 2) * (x ** 2))  # A, de 0 a 1 = 0.34134474606; de 0 a 5 = 0.49999971334

print "Exercicio 2:\n\n"
N = input("Digite a quantidade de pontos de integracao (entre 1 e 10): ")
print

I1 = PolynomialIntegration(f, 0.0, 1.0, N)
print
I2 = PolynomialIntegration(f, 0.0, 5.0, N)
print "\nI1 =", I1
print "I2 =", I2, "\n"

I1 = GaussianIntegration(f, 0.0, 1.0, N)
print
I2 = GaussianIntegration(f, 0.0, 5.0, N)
print "\nI1 =", I1
print "I2 =", I2

raw_input()
