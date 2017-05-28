from numpy import array

#Referencia da matriz abaixo: https://archive.lib.msu.edu/crcmath/math/math/n/n080.htm
#Matriz de pesos a serem multiplicados por DELTA, NAO POR L. Estes pesos nao incluem a divisao por N - 1 "embutida".
weights = [[0 for x in range(10)] for y in range(10)] #inicializando matriz de pesos com zeros
weights[0][0] = 1.0
weights[1][0:2] = 1.0 / 2 * array([1, 1])
weights[2][0:3] = 1.0 / 3 * array([1, 4, 1])
weights[3][0:4] = 3.0 / 8 * array([1, 3, 3, 1])
weights[4][0:5] = 2.0 / 45 * array([7, 32, 12, 32, 7])
weights[5][0:6] = 5.0 / 288 * array([19, 75, 50, 50, 75, 19])
weights[6][0:7] = 1.0 / 140 * array([41, 216, 27, 272, 27, 216, 41])
weights[7][0:8] = 7.0 / 17280 * array([751, 3577, 1323, 2989, 1502, 2989, 1323, 3577, 751])
weights[8][0:9] = 4.0 / 14175 * array([989, 5888, -928, 10496, -4540, 10496, -928, 5888, 989])
weights[9][0:10] = 9.0 / 89600 * array([2857, 15741, 1080, 19344, 5788, 5788, 19344, 1080, 15741, 2857])

def PolynomialIntegrate(f, a, b, N):
    print "\nIntegracao polinomial (Newton-Cotes) com",N,"ponto(s) ..."
    L = delta = b-a
    if (N > 1):
        delta = L/(N-1.0)
    print "a =",a,"; b =",b,"; L =",L,"; delta =",delta,"..."
    x_i = []
    if (N < 2):
        x_i.append((a+b)/2.0)
    else:
        for i in range(0,N):
            x_i.append(a+(i)*delta)
    #print "Pontos de integracao numerica:",x_i,"..."
    A=0.0
    w_i = weights[N-1]
    #print "Pesos para integracao numerica:",w_i,"..."
    for i in range(0,N):
        A += w_i[i] * delta * f(x_i[i])
    print "Resultado: A =",A
    return A