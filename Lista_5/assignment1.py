from numericalData import *


def PolynomialIntegration(f, a, b, N):
    print "Quadratura polinomial (Newton-Cotes) com",N,"ponto(s) ...."
    L = delta = b - a
    if N > 1:
        delta = L / (N - 1.0)
    print "a =", a, "; b =", b, "; L =", L, "; delta =", delta, "...."
    x_i = []
    if N < 2:
        x_i.append((a + b) / 2.0)
    else:
        for i in range(0, N):
            x_i.append(a + (i) * delta)
    w_i = PolynomialWeights[N - 1]
    # print "Pontos de integracao numerica:",x_i,"...."
    # print "Pesos para integracao numerica:",w_i,"...."
    A = 0.0
    for i in range(0, N):
        A += w_i[i] * delta * f(x_i[i])
    print "Resultado: A =", A
    return A


def NormalGaussianIntegration(g, a, b, N):
    if (a != -1) or (b != 1):
        return "Dominio de integracao nao normalizado (!= de -1 a 1). Saindo ...."
    print "Quadratura gaussiana normal com",N, "ponto(s) ...."
    print "a =",a,"; b =",b,"...."
    z_i = NormalGaussianPoints[N - 1]
    w_i = NormalGaussianWeights[N - 1]
    # print "Pontos de integracao numerica:",z_i,"...."
    # print "Pesos para integracao numerica:",w_i,"...."
    A = 0.0
    for i in range(0, N):
        A += w_i[i] * g(z_i[i])
    print "Resultado: A =", A
    return A


def GaussianIntegration(f, a, b, N):
    if (a == -1) and (b == 1):
        NormalGaussianIntegration(f, a, b, N)
    else:
        print "Quadratura gaussiana (Gauss-Legendre) com",N,"ponto(s) ...."
        L = b - a
        print "a =",a,"; b =",b,"; L =",L, "...."
        z_i = NormalGaussianPoints[N - 1]
        w_i = NormalGaussianWeights[N - 1]
        x_i = []
        for i in range(0, N):
            x_i.append( 0.5 * ( a + b + z_i[i]*L ) )
        # print "Pontos de integracao numerica:",x_i,"...."
        # print "Pesos para integracao numerica:",w_i,"...."
        A = 0.0
        for i in range(0, N):
            A += w_i[i] * f(x_i[i])
        A = (L / 2) * A
        print "Resultado: A =", A
        return A