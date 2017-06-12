# coding=utf-8
from numericalData import *


def PolynomialIntegration(f, a, b, N):
    print "Quadratura polinomial (Newton-Cotes) com", N, "ponto(s) ...."
    # Auto-explicativo
    L = delta_x = b - a
    # Se N == 1, aplicamos a regra do mid-point e a operação abaixo não se aplica
    if N > 1:
        delta_x = L / (N - 1.0)
    print "a =", a, "; b =", b, "; L =", L, "; delta_x =", delta_x, "...."
    x_i = []
    if N < 2:
        # Se N == 1, aplicamos a regra do mid-point, não há iteração
        x_i.append((a + b) / 2.0)
    else:
        for i in range(0, N):
            # X(i+1) = a + i*delta_x, como no slide
            x_i.append(a + i * delta_x)
    # Pegando a linhas da matriz de pesos correspondente ao número de pontos N
    w_i = PolynomialWeights[N - 1]
    # print "Pontos de integracao numerica:",x_i,"...."
    # print "Pesos para integracao numerica:",w_i,"...."
    A = 0.0
    for i in range(0, N):
        # Somatório que aproxima área sob a curva. Definição difere um pouco do slides
        # porque pesos utilizados aqui não foram dividos por delta de antemão.
        A += w_i[i] * delta_x * f(x_i[i])
    print "Resultado: A =", A
    return A


def NormalGaussianIntegration(g, a, b, N):
    if (a != -1) or (b != 1):
        return "Dominio de integracao nao normalizado (!= de -1 a 1). Saindo ...."
    print "Quadratura gaussiana normal com", N, "ponto(s) ...."
    print "a =", a, "; b =", b, "...."
    # Pegamos Zi e Wi correspondentes a N pontos de integração
    z_i = NormalGaussianPoints[N - 1]
    w_i = NormalGaussianWeights[N - 1]
    # print "Pontos de integracao numerica:",z_i,"...."
    # print "Pesos para integracao numerica:",w_i,"...."
    A = 0.0
    for i in range(0, N):
        # Definição idêntica aos slides, quando o domínio é normalizado
        A += w_i[i] * g(z_i[i])
    print "Resultado: A =", A
    return A


def GaussianIntegration(f, a, b, N):
    # Se domínio de integração é normalizado então...
    if (a == -1) and (b == 1):
        NormalGaussianIntegration(f, a, b, N)
    else:
        print "Quadratura gaussiana (Gauss-Legendre) com", N, "ponto(s) ...."
        # Auto-explicativo, direto dos slides
        L = b - a
        print "a =", a, "; b =", b, "; L =", L, "...."
        # Pegamos Zi e Wi correspondentes a N pontos de integração
        z_i = NormalGaussianPoints[N - 1]
        w_i = NormalGaussianWeights[N - 1]
        x_i = []
        for i in range(0, N):
            # Definição de normalização de Xi idêntica aos slides
            x_i.append(0.5 * (a + b + z_i[i] * L))
        # print "Pontos de integracao numerica:",x_i,"...."
        # print "Pesos para integracao numerica:",w_i,"...."
        A = 0.0
        for i in range(0, N):
            # Definição idêntica aos slides, quando o domínio é normalizado
            # pois normalizamos o domínio nas instruções acima
            A += w_i[i] * f(x_i[i])
        A = (L / 2) * A
        print "Resultado: A =", A
        return A
