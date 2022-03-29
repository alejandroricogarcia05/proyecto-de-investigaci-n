from random import  *

print(random()) #Devuelve un valor en [0.0, 1.0)

print(uniform(2.0,10.0)) #Devuelve un valor en [2.0, 10.0]

print(randrange(10)) #Devuelve valores enteros 0 y 9 (no incluye 10)

print(randrange(0, 101, 2))  #Devuelve valores enteros de 0 a 100 que sean pares

print(choice(['piedra', 'papel', 'tijera'])) #Devuelve uno de los tres valores