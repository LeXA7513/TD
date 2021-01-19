point = (5,6)
#        x,y
print(point)
from collections import namedtuple

Point2D = namedtuple ("Point2D",["x","y"])

p0 = Point2D(0.5,0.5)

print(p0)

def norme(p):
  d2 = p[0]**2 + p[1]**2
  return d2**0.5

print(norme(point))

point1=(0,0)
point2=(1,1)


print(norme(point1))
print(norme(point2))
print(norme((0,1)))
print(norme(p0))

p1 = Point2D(1,1)

print(f"{p0} + {p1} = {p0+p1}")

nombre = 9.0
carre = nombre**2
print("Le carré de", nombre,"vaut", carre)

message_carr = f"Le carré de {nombre} vaut {nombre**2}"

print(message_carr)