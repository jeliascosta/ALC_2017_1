# f(x) = 1 / (1 + x**2)
# L = b-a = 3-0 = 3
# Pela regra do ponto medio:
#   x1 = (0+3)/2 = 1.5
#   w1 = L = 3
#   integral, de 0 a 3 = w1*f(x1) = 3*f(1.5) = 3 * 0.30769... = 0.92308... = M(f)
# Pela regra do trapezio:
#    x1 = a = 0; x2 = b = 3
#    w1 = w2 = L/2 = 3/2 = 1.5
#    integral, de 0 a 3 = w1*f(x1) + w2*f(x2) = 1.5 * (f(0) + f(3)) = 1.5 * (1 + 0.1) = 1.5 * 1.1 = 1.65 = T(f)
# Relacao entre a regra de Simpson ( S(f) ) e as regras do ponto medio ( M(f) ) e do trapezio ( T(f) )
#    S(f) = (2/3)*M(f) + (1/3)*T(f)
#    Estimando integral, de 0 a 3, por Simpson, dadas as relacoes acima:
#       (2/3)*0.92308 + (1/3)*(1.65) =  1,165386666....7 = S(f)


from math import ceil
from assignment1 import PolynomialIntegration, GaussianIntegration


def f(x):
    return 1 / (1 + x**2)  # A, de 0 a 3 = 1.24905....


print "Exercicio 6:\n\n"
A = PolynomialIntegration(f, 0.0, 3.0, 1) #mid-point
print
A = PolynomialIntegration(f, 0.0, 3.0, 2) #trapezio
print
A = PolynomialIntegration(f, 0.0, 3.0, 3) #Simpson
print
A = PolynomialIntegration(f, 0.0, 3.0, 10) #Maximo de pontos
print
A = GaussianIntegration(f, 0.0, 3.0, 10) #Maximo de pontos por Gauss

print '''
Os valores obtidos pelo calculo numerico manual (comentario no inicio do arquivo)
e pelo computacional foram precisamente os mesmos!
'''
raw_input()
