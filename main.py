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

def ajout_point(p_1, p_2):
  p3_x =p_1[0]+p_2[0]
  p3_y =p_1[1]+p_2[1]
  return Point2D(p3_x,p3_y)
print(f"{p0} + {p1} = {ajout_point(p0,p1)}")