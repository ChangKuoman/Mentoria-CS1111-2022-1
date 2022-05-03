
### INTRODUCCION ###

# functions
from math import pi

def hallar_area(radio):
    circulo = pi * radio ** 2
    cuadrado = radio * radio
    return circulo, cuadrado

ci1, cu1 = hallar_area(9)

ci2, cu2 = hallar_area(5)

print(hallar_area(8))

print(ci1)
print(cu1)

var1, var2 = 8, 6
print(var1, var2)
