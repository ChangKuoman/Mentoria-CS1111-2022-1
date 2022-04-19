
### EJERCICIO DE PC ###

"""
Un valor es válido si pertenece al intervalo de 1 a 20 inclusive. Ingresar varios números emitiendo el
 mensaje correspondiente (“válido”, “no válido”) para cada uno y terminar cuando se hayan ingresado tres (3)
 números válidos.
"""

count_validos = 0

while count_validos < 3:
    n = int(input("Ingrese numero: "))
    if 0 < n < 21:
        print("valido")
        count_validos += 1
    else:
        print("no valido")
