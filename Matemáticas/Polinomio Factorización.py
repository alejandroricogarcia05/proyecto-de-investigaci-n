from sympy import *

x = symbols('x')

polinomio = 2*x**2 - 5*x - 3 #Declaración del polinomio

print(factor(polinomio)) #(x - 3)*(2*x + 1)
