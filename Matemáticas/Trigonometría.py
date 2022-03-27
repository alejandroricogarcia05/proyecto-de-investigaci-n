from sympy import *
from math import *

a = symbols('a') #Cateto contiguo

b = 30 #Cateto opuesto

c = symbols('c') #Hipotenusa


#Supongamos que tenemos un triángulo de 30 grados donde solo sabemos su cateto opuesto.

eqC = Eq(sin(radians(30)), b/c) #sen(30) = b/c
eqA = Eq(tan(radians(30)),b/a) #tg(30) = b/a
 
print(solve(eqC)) #[60.0000000000000]
print(solve(eqA)) #[51.9615242270663]

print(solve((eqC,eqA),(a,c))) # {c: 60.0000000000000, a: 51.9615242270663}

#Este método une todos las letras del resultado en un solo número

#join() une todas los números mientras que map() los convierte en letras

eqCstring = ''.join(map(str,solve(eqC)))
eqAstring = ''.join(map(str,solve(eqA)))

#float() reconvierte el valor string otra vez a un número decimal

print(float(eqCstring)) # 60.0
print(float(eqAstring)) # 51.9615242270663