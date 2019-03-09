from numpy import ones, vstack
from numpy.linalg import lstsq
from math import sqrt as sqrt

# import sys
# linex1 = input("Inserire la coordinata x del primo punto della linea: ")
# liney1 = input("Inserire la coordinata y del primo punto della linea: ")
# linex2 = input("Inserire la coordinata x del secondo punto della linea: ")
# liney2 = input("Inserire la coordinata y del secondo punto della linea: ")
# pointx1 = input("Inserire la coordinata x del punto: ")
# pointx2 = input("Inserire la coordinata x del punto: ")

pointsforline = [(2, 3), (9, 7)]

x_coords, y_coords = zip(*pointsforline)
print("coordinate x dei punti: {x}".format(x=x_coords))
print("coordinate y dei punti: {y}".format(y=y_coords))

# vstack serve per creare una sorta di matrice
# l'attributo .t crea la trasposta della matrice
A = vstack([x_coords, ones(len(x_coords))]).T
print(A)

m, c = lstsq(A, y_coords, rcond=-1)[0]
print("m = {m}".format(m=m))
print("c = {c}".format(c=c))

print("L'equazione della retta è y = {m}x + {c}".format(m=m, c=c))

point = (4, 6)

distanzanum = abs(point[1]-(m*point[0] + c))
print(distanzanum)
distanzaden = sqrt(1+m)
print(distanzaden)

distanzaris = distanzanum/distanzaden

print("la distanza fra la retta e il punto con coordinate ({x},{y}) è {d}".format(x=point[0], y=point[1], d=distanzaris))



