from numpy import ones, vstack
from numpy.linalg import lstsq
from math import sqrt

# pointsforline = [[], []], [[], []]
# point = [[], []]
# pointsforline[0][0] = input("Inserire la coordinata x del primo punto della linea: ")
# pointsforline[0][1] = input("Inserire la coordinata y del primo punto della linea: ")
# pointsforline[1][0] = input("Inserire la coordinata x del secondo punto della linea: ")
# pointsforline[1][1] = input("Inserire la coordinata y del secondo punto della linea: ")
# point[0] = input("Inserire la coordinata x del punto: ")
# point[1] = input("Inserire la coordinata x del punto: ")


class linesandpoints:

    def distancepointfromline(self):
        pointsforline = [(2, 3), (9, 7)]

        x_coords, y_coords = zip(*pointsforline)
        print("\ncoordinate x dei punti: {x}".format(x=x_coords))
        print("coordinate y dei punti: {y}".format(y=y_coords))

        # vstack serve per creare una sorta di matrice
        # l'attributo .t crea la trasposta della matrice
        A = vstack([x_coords, ones(len(x_coords))]).T
        print(A)

        m, c = lstsq(A, y_coords, rcond=-1)[0]
        print("\nm = {m}".format(m=m))
        print("c = {c}".format(c=c))

        print("\nL'equazione della retta è y = {m}x + {c}\n".format(m=m, c=c))

        point = (4, 6)

        distanzanum = abs(point[1]-(m*point[0] + c))
        print(distanzanum)
        distanzaden = sqrt(1+m)
        print(distanzaden)

        distanzaris = distanzanum/distanzaden

        print("\nla distanza fra la retta e il punto con coordinate ({x},{y}) è {d}".format(x=point[0], y=point[1], d=distanzaris))

        return

