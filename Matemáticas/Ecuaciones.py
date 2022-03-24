from sympy import * 

x = symbols('x') #Símbolo que queremos averiguar

ecuacion = Eq((2*x - 4),0)

print(solve(ecuacion)) # 2*x - 4 = 0

