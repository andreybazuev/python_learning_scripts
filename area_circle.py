import math
from distance import distance

def area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = math.pi * (radius ** 2)
    return result

print(area(1, 2, 4, 6))