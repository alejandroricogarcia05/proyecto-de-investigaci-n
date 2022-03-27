from sympy import *
from math import *

a = symbols('a') # Cateto contiguo

b = 30 # Cateto opuesto

c = symbols('c') # Hipotenusa


eqC = Eq(sin(radians(30)), b/c) #sen(30) = b/c
eqA = Eq(tan(radians(30)),b/a) #tg(30) = b/a
 
print(solve(eqC)) # [60.0000000000000]
print(solve(eqA)) # [51.9615242270663]

print(solve((eqC,eqA),(a,c))) # {c: 60.0000000000000, a: 51.9615242270663}

valueC = solve(eqC)
valueA = solve(eqA)

print(round(valueC[0])) # 60
print(round(valueA[0])) # 52