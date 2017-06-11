def Serie_Taylor(f, x_0, x_0_l, t_0, t_n, delta_t):
    print "Resolvendo por Expansao em Serie de Taylor ...."
    print "Condicao inicial: y(0) =", x_0, "; y'(0) = ", x_0_l, "; ", t_0, "<= t <", t_n, "; delta de t:", delta_t, "...."
    k = 0
    x_k = [x_0]
    x_k_l = x_0_l
    t_k = [t_0]
    while t_k[k] < t_n:
        x_k_ll = f(t_k[k], x_k[k], x_k_l)
        x_k.append(x_k[k] + x_k_l * delta_t + (delta_t ** 2.0) * x_k_ll / 2.0)  # inserindo x_k+1 na lista
        k = k + 1
        t_k.append(t_0 + k * delta_t)  # definicao completa de t_k. Valido para qualquer t_0, mesmo # 0
        x_k_l = x_k_l + delta_t * x_k_ll
    return [t_k, x_k]


def Runge_Kutta_Nystrom(f, x_0, x_0_l, t_0, t_n, delta_t):
    print "Resolvendo pelo metodo de Runge-Kutta-Nystrom ...."
    print "Condicao inicial: y(0) =", x_0, "; y'(0) = ", x_0_l, "; ", t_0, "<= t <", t_n, "; delta de t:", delta_t, "...."
    k = 0
    x_k = [x_0]
    x_k_l = x_0_l
    t_k = [t_0]
    hh = delta_t / 2.0  # half h
    while t_k[k] < t_n:
        K1 = hh * f(t_k[k], x_k[k], x_k_l)
        Q = hh * (x_k_l + K1 / 2.0)
        K2 = hh * f(t_k[k] + hh, x_k[k] + Q, x_k_l + K1)
        K3 = hh * f(t_k[k] + hh, x_k[k] + Q, x_k_l + K2)
        L = delta_t * (x_k_l + K3)
        K4 = hh * f(t_k[k] + delta_t, x_k[k] + L, x_k_l + 2 * K3)
        x_k.append(x_k[k] + delta_t * (x_k_l + (K1 + K2 + K3)/3.0))  # inserindo x_k+1 na lista
        k = k + 1
        t_k.append(t_0 + k * delta_t)  # definicao completa de t_k. Valido para qualquer t_0, mesmo # 0
        x_k_l = x_k_l + (K1 + 2*K2 + 2*K3 + K4)/3.0
    return [t_k, x_k]
