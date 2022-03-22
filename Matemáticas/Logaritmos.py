import math
import sympy

n = 2 # Base
p = 8 # Argumento 

# math.log(Argumento, Base)

print(math.log(8,2)) # 3

x = sympy.symbols('x') #Símbolo que queremos averiguar

#La función que vamos a utilizar
def Logaritmo(Base, Argumento):
    ecuacion = (sympy.Eq(Base**x,Argumento))  #Declaración
    print(sympy.solve(ecuacion)) #Resultado

Logaritmo(n,p) #3