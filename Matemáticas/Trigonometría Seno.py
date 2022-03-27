from sympy import *
from math import radians, degrees


#Lado a y su ángulo opuesto
a = 5.99
alpha = symbols('alpha')

#Lado b y su ángulo opuesto
b = 5.07
beta = 50

#Lado c y su ángulo opuesto
c = symbols('c')
y = 65

eqA = Eq(a/sin(alpha),b/sin(radians(beta))) # a/sen(alpha) = b/sen(beta)
eqB = Eq(b/sin(radians(beta)),c/sin(radians(y))) # b/sen(beta) = c/sen(y) 



print("alpha =", solve(eqA)) # alpha = [1.13149852804901, 2.01009412554079]
print("c =", solve(eqB)) # c = [5.99832101329159]

valueA = solve(eqA)
valueB = solve(eqB)


print(degrees(valueA[0])) # 64.83009018247306
print(degrees(valueA[1])) # 115.16990981752696
print(valueB[0]) # 5.99832101329159