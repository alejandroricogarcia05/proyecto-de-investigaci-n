from sympy import *

x = symbols('x')

#Declaración de inecuaciones
a = x**2 + 6*x < 0 
b = x**2 + 6*x > 0 
c = x**2 + 6*x <= 0 
d = x**2 + 6*x >= 0 


print(solveset(a,x,S.Reals)) #Interval.open(-6, 0)
print(solveset(b,x,S.Reals)) #Union(Interval.open(-oo, -6), Interval.open(0, oo))
print(solveset(c,x,S.Reals)) #Interval(-6, 0)
print(solveset(d,x,S.Reals)) #Union(Interval(-oo, -6), Interval(0, oo))

print ('\n')

print(solve(a,x,S.Reals)) #(-6 < x) & (x < 0)
print(solve(b,x,S.Reals)) #((-oo < x) & (x < -6)) | ((0 < x) & (x < oo))
print(solve(c,x,S.Reals)) #(-6 <= x) & (x <= 0)
print(solve(d,x,S.Reals)) #((0 <= x) & (x < oo)) | ((-oo < x) & (x <= -6))

print ('\n')

e = x - 2 > 0
f = x - 1 < 3

print(solve((e,f),x,S.Reals)) # (2 < x) & (x < 4)