
### EJERCICIO ###

# strings
"""
Implemente un algoritmo que permita generar un string a partir de otro inter-
calando una palabra en may ́usculas y otra en m ́ın ́usculas. Adicionalmente reemplace la

ocurrencia de las vocales por asteriscos.
Algunos ejemplos de di ́alogo de este programa ser ́ıan:
Input : Hola Juan como estas
Output : H * L * j ** n C * M * * st * s
Input : Peru pais de todas las sangres
Output : P * R * p ** s D * t *d * s L * S s * ngr * s
"""

cadena = str(input("Input: "))

nueva_cadena = ""
for i in range(len(cadena)):
    if i % 2 == 0:
        nueva_cadena += cadena[i].upper()
    else:
        nueva_cadena += cadena[i].lower()

nueva_cadena2 = ""
for i in range(len(nueva_cadena)):
    if nueva_cadena[i] in "aeiouAEIOU":
        nueva_cadena2 += '*'
    else:
        nueva_cadena2 += nueva_cadena[i]

print(nueva_cadena2)
