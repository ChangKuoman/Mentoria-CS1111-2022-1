
### EJERCICIO ###

# Ingresar el <radio> y la <altura> de un cilindro y hallar el volumen del sólido

import math

radio = float(input("Ingrese radio: "))
altura = float(input("Ingrese altura: "))

volumen = math.pow(math.pi * radio, 2) * altura
# math.pow( base , exponente )

print(f"El volumen del cilindro es {volumen} u^3")

print(math.pi)
print(math.e)
