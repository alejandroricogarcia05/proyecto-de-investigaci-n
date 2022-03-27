from sympy import *
from math import radians, degrees

#Los lados
a = 5
b = 6
c = 7

#Los ángulos
alpha = symbols('alpha')
beta = symbols('beta')
y = symbols ('y')

eqA = Eq(c**2, a**2 + b**2 -2*a*b*cos(alpha)) 
eqB = Eq(b**2, a**2 + c**2 - 2*a*c*cos(beta)) 
eqY = Eq(a**2, b**2 + c**2 - 2*b*c*cos(y))

valueA = solve(eqA)
valueB = solve(eqB)
valueY = solve(eqY)

# Sabemos que van a haber 2**3 resultados, por lo tanto vamos a utilizar bucles de control
# para organizarlos todos y pasar el resultado a grados.

for x in valueA:
    print("A:", degrees(x)) #A: 281.5369590328155
                            #A: 78.46304096718453
print("\n")
for x in valueB:
    print("B:", degrees(x)) #B: 302.8783495643775
                            #B: 57.12165043562251
print("\n")
for x in valueY:
    print("Y:", degrees(x)) #Y: 315.58469140280704
                            #Y: 44.415308597192976