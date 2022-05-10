
### EJERCICIO ###

"""
2021-2 UPCH Lab9.2
6. Escriba un programa que reciba dos cadenas de caracteres del teclado y realice lo siguiente:
Intercambiar los dos primeros caracteres de cada cadena y concatenar las cadenas resultantes en una
sola cadena en la que cada cadena esté separada por un espacio.
Ingrese la primera cadena: "abcdefg"
Ingrese la segunda cadena: "vwxyz"
La nueva cadena es: "vwcdefg abxyz"
"""

cadena1 = str(input("Ingrese cadena1: "))
cadena2 = str(input("Ingrese cadena2: "))

cadena_resultante = cadena2[0:2] + cadena1[2::] + " " + cadena1[0:2] + cadena2[2::]
print(cadena_resultante)
