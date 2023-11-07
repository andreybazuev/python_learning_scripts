#вычисление гипотенузы по заданным длинам катетов

import math

def hypotenuse(k1, k2):
    return(math.sqrt(k1**2 + k2**2))

print("Гипотенуза равна:", hypotenuse(3, 5))
print("Гипотенуза равна:", hypotenuse(6, 1))