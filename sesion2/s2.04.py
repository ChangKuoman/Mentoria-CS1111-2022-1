
### EJERCICIO ###

# Genere un <número al azar> del 1 al 20 haciendo uso de la librería random
# e indique si es menor o igual a 10 o no.

from random import randint, uniform, random
"""
azar = randint(1, 20)
azar2 = uniform(10, 12)
azar3 = random()
azar_letra = chr(randint(65, 90))
# char | caracter => a    H    t    @
# string => hola

print(azar)
print(azar2)
print(azar3)
print(azar_letra)
"""

numero_azar = randint(1, 20)
print(numero_azar)
if numero_azar < 10:
    print("Es menor que 10.")
else:
    print("Es mayor que 10.")
