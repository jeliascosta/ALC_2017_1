def f(t, x):
    # return x
    # return t + x
     return -2 * t * x ** 2


def Euler(x_0, t_0, t_n, delta_t):
    print "Resolvendo pelo metodo de Euler ...."
    print "Condicao inicial: y(0)=", x_0, "; ", t_0, "<= t <", t_n, "; delta de t:", delta_t,"...."
    k = 0
    # Condição inicial y(t), t = t_0, fornecida para o algoritmo
    x_k = [x_0]
    t_k = t_0
    while t_k < t_n:
        # Definição de Xk+1 idêntica aos slides. K1 foi suprimido por simplificação.
        x_k.append(x_k[k] + delta_t * f(t_k, x_k[k]))
        k = k + 1
        # Definição de Tk mais completa que os slides. Válido para qualquer T0, não só igual a 0.
        t_k = t_0 + k * delta_t
    return x_k[-1]


def Runge_Kutta_2ordem(x_0, t_0, t_n, delta_t):
    print "Resolvendo pelo metodo de Runge-Kutta de 2a ordem ...."
    print "Condicao inicial: y(0)=", x_0, "; ", t_0, "<= t <", t_n, "; delta de t:", delta_t,"...."
    k = 0
    # Condição inicial y(t), t = t_0, fornecida para o algoritmo
    x_k = [x_0]
    t_k = t_0
    while t_k < t_n:
        K1 = f(t_k, x_k[k])
        K2 = f(t_k + delta_t, x_k[k] + delta_t * K1)
        # Definição de Xk+1 idêntica aos slides.
        x_k.append(x_k[k] + (delta_t / 2.0) * (K1 + K2))
        k = k + 1
        # Definição de Tk mais completa que os slides. Válido para qualquer T0, não só igual a 0.
        t_k = t_0 + k * delta_t
    return x_k[-1]


def Runge_Kutta_4ordem(x_0, t_0, t_n, delta_t):
    print "Resolvendo pelo metodo de Runge-Kutta de 4a ordem ...."
    print "Condicao inicial: y(0)=", x_0, "; ", t_0, "<= t <", t_n, "; delta de t:", delta_t,"...."
    k = 0
    # Condição inicial y(t), t = t_0, fornecida para o algoritmo
    x_k = [x_0]
    t_k = t_0
    while t_k < t_n:
        K1 = f(t_k, x_k[k])
        K2 = f(t_k + delta_t/2.0, x_k[k] + (delta_t/2.0) * K1)
        K3 = f(t_k + delta_t/2.0, x_k[k] + (delta_t/2.0) * K2)
        K4 = f(t_k + delta_t, x_k[k] + delta_t * K3)
        # Definição de Xk+1 idêntica aos slides.
        x_k.append(x_k[k] + (delta_t / 6) * (K1 + 2*K2 + 2*K3 + K4))  # inserindo x_k+1 na lista
        k = k + 1
        # Definição de Tk mais completa que os slides. Válido para qualquer T0, não só igual a 0.
        t_k = t_0 + k * delta_t
    return x_k[-1]


print '''
Lista 6
Exercicio 1

*OBS: Resposta exata --> y(2) = 0.2

Escolha um metodo numerico para resolver a equacao diferencial:
1. Euler, passo de integracao = 0.1
2. Runge-Kutta segunda ordem, passo de integracao = 0.1
3. Runge-Kutta quarta ordem, passo de integracao = 0.1
4. Todos, passos de integracao otimizados
'''

C = input()

if C == 1:
    y_2 = Euler(1.0, 0.0, 2.0, 0.1)
    print "y(2) = ",y_2
if C == 2:
    y_2 = Runge_Kutta_2ordem(1.0, 0.0, 2.0, 0.1)
    print "y(2) = ",y_2
if C == 3:
    y_2 = Runge_Kutta_4ordem(1.0, 0.0, 2.0, 0.1)
    print "y(2) = ",y_2
if C == 4:
    y_2 = Euler(1.0, 0.0, 2.0, 0.00001)
    print "y(2) = ",y_2,"\n"
    y_2 = Runge_Kutta_2ordem(1.0, 0.0, 2.0, 0.01)
    print "y(2) = ",y_2,"\n"
    y_2 = Runge_Kutta_4ordem(1.0, 0.0, 2.0, 0.1)
    print "y(2) = ",y_2,"\n"