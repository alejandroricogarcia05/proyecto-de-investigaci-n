from sympy import *
from sympy.calculus.util import continuous_domain

x = Symbol("x")

f = 2*x - 4 # Declaración de la función

print(f.subs(x,2)) # 0
print(f.subs(x,3)) # 2
print(f.subs(x,4)) # 4

print(continuous_domain(f,x,S.Reals)) #Reals (Dominio es todos los números reales)

g = 2/x 

print(continuous_domain(g,x,S.Reals)) #Union(Interval.open(-oo, 0), Interval.open(0, oo))

p1 = plot(f) 
p2 = plot(g)
