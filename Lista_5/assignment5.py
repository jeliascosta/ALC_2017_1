from math import ceil
from assignment1 import PolynomialIntegration, GaussianIntegration


def minPolynomialN(degree):
    return degree + 1  # "N pontos de integracao integram exatamente qualquer polinomio de grau N-1."


def minGaussianN(degree):
    return int(ceil((degree + 1.0) / 2.0))  # "Com N pontos de integracao integra-se exatamente um polinomio de grau (2N-1)"


def f(x):
    return 2 + 2 * x - x ** 2 + 3 * (x ** 3)  # A, de 0 a 4 = 194.666666666667


print "Exercicio 5:\n\n"
print "Para integracao exata de f(x), polinomio de grau 3, precisaremos de:"
print minPolynomialN(3), "pontos para integracao polinomial e"
print minGaussianN(3), "pontos para integracao gaussiana.\nDe fato, segue que:\n"
A = PolynomialIntegration(f, 0.0, 4.0, minPolynomialN(3))
print
A = GaussianIntegration(f, 0.0, 4.0, minGaussianN(3))

raw_input()
