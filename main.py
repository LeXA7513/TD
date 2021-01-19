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