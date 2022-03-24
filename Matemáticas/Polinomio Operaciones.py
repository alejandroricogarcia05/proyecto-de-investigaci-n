from sympy import *

x = symbols('x')

a = 2*x**2 - 5*x - 3 
b = 4*x**2 + 6*x + 2

print(a+b) # 6*x**2 + x - 1
print(a-b) # -2*x**2 - 11*x - 5

print(Poly.mul(poly(a),poly(b)).as_expr()) # 8*x**4 - 8*x**3 - 38*x**2 - 28*x - 6
print(div(a,a)) # (1/2, -8*x - 4)