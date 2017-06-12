# coding=utf-8
def Serie_Taylor(f, x_0, x_0_l, t_0, t_n, delta_t):
    print "Resolvendo por Expansao em Serie de Taylor ...."
    print "Condicao inicial: y(0) =", x_0, "; y'(0) = ", x_0_l, "; ", t_0, "<= t <", t_n, "; delta de t:", delta_t, "...."
    k = 0
    # Condição inicial y(t), t = t_0, fornecida para o algoritmo
    x_k = [x_0]
    # Condição inicial y'(t), t = t_0, fornecida para o algoritmo
    x_k_l = x_0_l
    # Guardamos os Ti para plotar os gráficos e tabelas
    t_k = [t_0]
    while t_k[k] < t_n:
        #Definição de Xk+1'' idêntica aos slides
        x_k_ll = f(t_k[k], x_k[k], x_k_l)
        # Definição de Xk+1 idêntica aos slides.
        x_k.append(x_k[k] + x_k_l * delta_t + (delta_t ** 2.0) * x_k_ll / 2.0)
        k = k + 1
        # Definição de Tk mais completa que os slides. Válido para qualquer T0, não só igual a 0.
        t_k.append(t_0 + k * delta_t)
        #Definição de Xk+1' idêntica aos slides
        x_k_l = x_k_l + delta_t * x_k_ll
    return [t_k, x_k]


def Runge_Kutta_Nystrom(f, x_0, x_0_l, t_0, t_n, delta_t):
    print "Resolvendo pelo metodo de Runge-Kutta-Nystrom ...."
    print "Condicao inicial: y(0) =", x_0, "; y'(0) = ", x_0_l, "; ", t_0, "<= t <", t_n, "; delta de t:", delta_t, "...."
    k = 0
    # Condição inicial y(t), t = t_0, fornecida para o algoritmo
    x_k = [x_0]
    # Condição inicial y'(t), t = t_0, fornecida para o algoritmo
    x_k_l = x_0_l
    # Guardamos os Ti para plotar os gráficos e tabelas
    t_k = [t_0]
    # Para não repetir delta_t/2 em todos os cálculos abaixo,
    # me permiti esta simplificação
    hh = delta_t / 2.0
    while t_k[k] < t_n:
        #Definições intermediárias idênticas aos slides
        K1 = hh * f(t_k[k], x_k[k], x_k_l)
        Q = hh * (x_k_l + K1 / 2.0)
        K2 = hh * f(t_k[k] + hh, x_k[k] + Q, x_k_l + K1)
        K3 = hh * f(t_k[k] + hh, x_k[k] + Q, x_k_l + K2)
        L = delta_t * (x_k_l + K3)
        K4 = hh * f(t_k[k] + delta_t, x_k[k] + L, x_k_l + 2 * K3)
        # Definição de Xk+1 idêntica aos slides.
        x_k.append(x_k[k] + delta_t * (x_k_l + (K1 + K2 + K3)/3.0))
        k = k + 1
        # Definição de Tk mais completa que os slides. Válido para qualquer T0, não só igual a 0.
        t_k.append(t_0 + k * delta_t)
        #Definição de Xk+1' idêntica aos slides
        x_k_l = x_k_l + (K1 + 2*K2 + 2*K3 + K4)/3.0
    return [t_k, x_k]
