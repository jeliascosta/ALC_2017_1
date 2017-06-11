import pylab as graphs
from math import fabs
from tabulate import tabulate
from assignment2 import Serie_Taylor, Runge_Kutta_Nystrom

g = 9.8105  # m/s^2
kD = 1.0


def f(t, x, x_l):
    return -g - kD * x_l * fabs(x_l)


print '''
Lista 6
Exercicio 2

*OBS: Resposta exata --> y(100) = 6.0

Escolha um metodo numerico para resolver a equacao diferencial de 2 ordem:
1. Expansao em Serie de Taylor, passo de integracao = 0.1
2. Runge-Kutta-Nystrom, passo de integracao = 0.1
3. Itens 1 e 3 com resultados tabelados, passo de integracao = 0.1
4. Item 1 com grafico evidenciando convergencia
5. Item 3 com grafico evidenciando convergencia
'''

C = input()
gt = ["r--", "g", "b--", "r", "g--", "b"]
if C == 1:
    y_Taylor = Serie_Taylor(f, 0.0, 0.0, 0.0, 20.0, 0.1)
    print "y(20) = ", y_Taylor[1][-1]
if C == 2:
    y_RKN = Runge_Kutta_Nystrom(f, 0.0, 0.0, 0.0, 20.0, 0.1)
    print "y(20) = ", y_RKN[1][-1]
if C == 3:
    y_Taylor = Serie_Taylor(f, 0.0, 0.0, 0.0, 20.0, 0.1)
    y_RKN = Runge_Kutta_Nystrom(f, 0.0, 0.0, 0.0, 20.0, 0.1)
    table = []
    for i in range(0, len(y_Taylor[0])):
        table.append([y_Taylor[0][i], y_Taylor[1][i], y_RKN[1][i]])
    headers = ["t", "y(t) por Taylor", "y(t) por RKN"]
    print "\n\n",tabulate(table, headers, tablefmt="fancy_grid")
if C == 4:
    delta_t = 0.4
    i = 0
    while delta_t > 0.001:
        result = Serie_Taylor(f, 0.0, 0.0, 0.0, 20.0, delta_t)
        print result[0][-1]
        print result[1][-1]
        lb = 'h = ' + str(delta_t)
        graphs.plot(result[0], result[1], gt[i % 6], label=lb)
        delta_t = delta_t / 4.0
        i = i + 1
    graphs.xlabel('Eixo t')
    graphs.ylabel('Eixo y')
    graphs.xlim(0.0, 21.0)
    graphs.ylim(-70.0, 1.0)
    graphs.legend()
    graphs.title("Convergencia da Expansao em Serie de Taylor")
    graphs.show()
if C == 5:
    delta_t = 0.4
    i = 0
    while delta_t >= 0.001:
        result = Runge_Kutta_Nystrom(f, 0.0, 0.0, 0.0, 20.0, delta_t)
        print result[0][-1]
        print result[1][-1]
        lb = 'h = ' + str(delta_t)
        graphs.plot(result[0], result[1], gt[i % 6], label=lb)
        delta_t = delta_t / 4.0
        i = i + 1
    graphs.xlabel('Eixo t')
    graphs.ylabel('Eixo y')
    graphs.xlim(0.0, 21.0)
    graphs.ylim(-70.0, 1.0)
    graphs.legend()
    graphs.title("Convergencia de Runge-Kutta-Nystrom")
    graphs.show()