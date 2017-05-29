from math import pi, sqrt, exp
from assignment1 import PolynomialIntegration, GaussianIntegration

N = 10  # Escolha arbitraria (maxima, neste caso)


def RAO(w):
    return 1.0 / (sqrt((1.0 - (w / w_n) ** 2.0) ** 2.0 + (2.0 * csi * w / w_n) ** 2.0))

#Exercicio 3
w_n = 1.0
csi = 0.05


def S_eta_as3(w):
    return 2


def S_sigma_as3(w):
    return ((RAO(w)) ** 2) * S_eta_as3(w)


def f_m0_as3(w):
    return S_sigma_as3(w)


def f_m2_as3(w):
    return (w ** 2) * S_sigma_as3(w)


def f_simplified(w):  # para testes
    return w ** 2 * 2 * (1 / sqrt(((1 - (w ** 2)) ** 2) + ((0.1 * w) ** 2))) ** 2

print "Exercicio 3:\n\n"
print "Calculando m0 por integracao polinomial ..."
m0 = PolynomialIntegration(f_m0_as3, 0.0, 10.0, N)
print "\nCalculando m2 por integracao polinomial ..."
m2 = PolynomialIntegration(f_m2_as3, 0.0, 10.0, N)
print "\nm0 =",m0
print "m2 =",m2,"\n"

print "Calculando m0 por integracao gaussiana ..."
m0 = GaussianIntegration(f_m0_as3, 0.0, 10.0, N)
print "\nCalculando m2 por integracao gaussiana ..."
m2 = GaussianIntegration(f_m2_as3, 0.0, 10.0, N)
print "\nm0 =",m0
print "m2 =",m2

# print(PolynomialIntegration(f_simplified,0,10,N))
# print(GaussianIntegration(f_simplified,0,10,N))

print "\n\nPressione Enter para executar o Exercicio 4"
raw_input()

#Exercicio 4
Hs = 3.0
Tz = 5.0


def S_eta_as4(w):
    if w == 0:
        return 0
    return exp(-((16*(pi**3))/((w**4)*(Tz**4)))) * ((4*(pi**3)*(Hs**2))/((w**5)*(Tz**4)))


def S_sigma_as4(w):
    return ((RAO(w)) ** 2) * S_eta_as4(w)


def f_m0_as4(w):
    return S_sigma_as4(w)


def f_m2_as4(w):
    return (w ** 2) * S_sigma_as4(w)

print "Exercicio 4:\n\n"
print "Calculando m0 por integracao polinomial ..."
m0 = PolynomialIntegration(f_m0_as4, 0.0, 10.0, N)
print "\nCalculando m2 por integracao polinomial ..."
m2 = PolynomialIntegration(f_m2_as4, 0.0, 10.0, N)
print "\nm0 =",m0
print "m2 =",m2,"\n"

print "Calculando m0 por integracao gaussiana ..."
m0 = GaussianIntegration(f_m0_as4, 0.0, 10.0, N)
print "\nCalculando m2 por integracao gaussiana ..."
m2 = GaussianIntegration(f_m2_as4, 0.0, 10.0, N)
print "\nm0 =",m0
print "m2 =",m2

raw_input()