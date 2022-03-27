from sympy import *
from math import radians, degrees

x = symbols('x')
y = symbols('y')

# trigsimp() Simplifica la razón trigonométrica
# expand_trig() Expande la razón trigonométrica

#Ejemplo:
print(trigsimp(sin(x)*cos(y) + sin(y)*cos(x))) # sin(x + y)
print(expand_trig(sin(x + y))) #sin(x)*cos(y) + sin(y)*cos(x)

print("\n")

#Razones del ángulo suma
print(expand_trig(sin(x + y))) # sin(x)*cos(y) + sin(y)*cos(x)
print(expand_trig(cos(x + y))) # -sin(x)*sin(y) + cos(x)*cos(y)
print(expand_trig(tan(x + y))) # (tan(x) + tan(y))/(-tan(x)*tan(y) + 1)

print("\n")

#Razones del ángulo diferencia
print(expand_trig(sin(x - y))) # sin(x)*cos(y) - sin(y)*cos(x)
print(expand_trig(cos(x - y))) # sin(x)*sin(y) + cos(x)*cos(y)
print(expand_trig(tan(x - y))) # (tan(x) - tan(y))/(tan(x)*tan(y) + 1)

print("\n")

#Razones del ángulo doble
print(expand_trig(sin(2*x))) # 2*sin(x)*cos(x)
print(expand_trig(cos(2*x))) # 2*sin(x)*cos(x)
print(expand_trig(tan(2*x))) # 2*tan(x)/(1 - tan(x)**2)
 
print("\n")

#Razones del ángulo mitad
print(expand_trig(sin(x/2)))
print(expand_trig(cos(x/2)))
print(expand_trig(tan(x/2)))

print("\n")

#Suma y diferencia de senos y cosenos
print(expand_trig(sin(x)+sin(y)))
print(expand_trig(sin(x)-sin(y)))
print(expand_trig(cos(x)+cos(y)))
print(expand_trig(sin(x)-cos(y)))



