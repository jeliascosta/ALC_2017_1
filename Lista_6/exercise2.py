import pylab as graphs
from math import sin, cos
from tabulate import tabulate
from assignment2 import Serie_Taylor, Runge_Kutta_Nystrom

m = 1.0
c = 0.2
k = 1.0
w = 0.5


def F(t):
    return 2 * sin(w * t) + sin(2 * w * t) + cos(3 * w * t)


def f(t, x, x_l):
    return (F(t) - c * x_l - k * x) * (1 / m)


print '''
Lista 6
Exercicio 2

*OBS: Resposta exata --> y(100) = 6.0

Escolha um metodo numerico para resolver a equacao diferencial de 2 ordem:
1. Expansao em Serie de Taylor, passo de integracao = 0.01
2. Runge-Kutta-Nystrom, passo de integracao = 0.01
3. Itens 1 e 3 com resultados tabelados, passo de integracao = 0.1
4. Item 1 com grafico evidenciando convergencia
5. Item 3 com grafico evidenciando convergencia
'''

C = input()
gt = ["r--", "g", "b--", "r", "g--", "b"]
if C == 1:
    y_Taylor = Serie_Taylor(f, 0.0, 0.0, 0.0, 100.0, 0.01)
    print "y(100) = ", y_Taylor[1][-1]
if C == 2:
    y_RKN = Runge_Kutta_Nystrom(f, 0.0, 0.0, 0.0, 100.0, 0.01)
    print "y(100) = ", y_RKN[1][-1]
if C == 3:
    y_Taylor = Serie_Taylor(f, 0.0, 0.0, 0.0, 100.0, 0.1)
    y_RKN = Runge_Kutta_Nystrom(f, 0.0, 0.0, 0.0, 100.0, 0.1)
    table = []
    for i in range(0, len(y_Taylor[0])):
        table.append([y_Taylor[0][i], y_Taylor[1][i], y_RKN[1][i]])
    headers = ["t", "y(t) por Taylor", "y(t) por RKN"]
    print "\n\n",tabulate(table, headers, tablefmt="fancy_grid")
if C == 4:
    delta_t = 0.3
    i = 0
    while delta_t > 0.001:
        result = Serie_Taylor(f, 0.0, 0.0, 0.0, 100.0, delta_t)
        print result[0][-1]
        print result[1][-1]
        lb = 'h = ' + str(delta_t)
        graphs.plot(result[0], result[1], gt[i % 6], label=lb)
        delta_t = delta_t / 4.0
        i = i + 1
    graphs.xlabel('Eixo t')
    graphs.ylabel('Eixo y')
    graphs.xlim(0.0, 105.0)
    graphs.ylim(-20.0, 20.0)
    graphs.legend()
    graphs.title("Convergencia da Expansao em Serie de Taylor")
    graphs.show()
if C == 5:
    delta_t = 2
    i = 0
    while delta_t >= 0.001:
        result = Runge_Kutta_Nystrom(f, 0.0, 0.0, 0.0, 100.0, delta_t)
        print result[0][-1]
        print result[1][-1]
        lb = 'h = ' + str(delta_t)
        graphs.plot(result[0], result[1], gt[i % 6], label=lb)
        delta_t = delta_t / 4.0
        i = i + 1
    graphs.xlabel('Eixo t')
    graphs.ylabel('Eixo y')
    graphs.xlim(0.0, 105.0)
    graphs.ylim(-11.0, 11.0)
    graphs.legend()
    graphs.title("Convergencia de Runge-Kutta-Nystrom")
    graphs.show()
