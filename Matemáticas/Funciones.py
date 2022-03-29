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

print(g.subs(x,0)) #Devuelve zoo que implica la división de cero. No para el programa.

#Les damos limites en los ejes x e y para que la gráfica se vea mejor.
p1 = plot(f,xlim=[-5,5],ylim=[-5,5]) 
p2 = plot(g,xlim=[-10,10],ylim=[-10,10])
