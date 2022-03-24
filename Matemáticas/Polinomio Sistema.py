from sympy import *

x = symbols('x')
y = symbols('y')

a = 2*x - y  # = 3
b = 4*x + 6*y  # = -2

eq1 = Eq(a,3)
eq2 = Eq(b,-2)

print(solve((eq1,eq2),(x,y)))