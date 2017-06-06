x_0 = 1; #teste

def dx_dt(t, x):
    return f(t, x);

def f(t, x):
    return x; #teste


def Euler():
    pass


def Runge_Kutta_2ordem():
    pass


def Runge_Kutta_4ordem():
    pass


print '''
Escolha o metodo de resolucao numerica da equacao diferencial:
1. Euler
2. Runge-Kutta segunda ordem
3. Runge-Kutta quarta ordem
'''

C = input()

if C == 1:
    Euler()
if C == 2:
    Runge_Kutta_2ordem()
if C == 3:
    Runge_Kutta_4ordem()
