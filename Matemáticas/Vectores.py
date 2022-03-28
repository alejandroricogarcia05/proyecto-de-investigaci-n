from numpy import *

vectorA = array([10,9])
vectorB = array([2,3])

#Suma y resta de vectores
print(vectorA+vectorB) #[12 12]
print(vectorA-vectorB) #[8 6]

#Producto escalar (10*2 + 9*3)
print(vectorA.dot(vectorB)) #47

Comb1 = 3 #Base 1
Comb2 = 5 # Base 2

#Combinación lineal
print (vectorA*Comb1 + vectorB*Comb2)

modA = linalg.norm(vectorA) 
modB = linalg.norm(vectorB)

#Módulos de los vectores
print('A:',modA,'B:', modB) #A: 13.45362404707371 B: 3.605551275463989

solucion = arccos((vectorA.dot(vectorB))/(modA*modB))

#Ángulo entre dos vectores
print(degrees(solucion))