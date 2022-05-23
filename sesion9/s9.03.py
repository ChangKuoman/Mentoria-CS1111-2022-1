
### EJERCICIO ###

# strings
"""
Implemente un algoritmo que permita generar un string a partir de otro in-
tercalando una palabra en may ́usculas y otra en min ́usculas. Cualquier otro car ́acter se

debe mantener. Asuma que no se combinar ́an letras y n ́umeros en una misma palabra.
Asimismo, asuma que solo habr ́a un espacio entre palabra y palabra.
Algunos ejemplos de di ́alogo de este programa ser ́ıan:
Input : Hola Juan como estas
Output : HOLA juan COMO estas
Input : tengo que aprobar el curso sacare 20
Output : TENGO que APROBAR el CURSO sacare 20
"""
# manera 1:
cadena = str(input("Input: "))

nueva_cadena = ""
# 'hola como estas' .split(' ')
# ['hola', 'como', 'estas']
mayuscula = True
for palabra in cadena.split(' '):
    if mayuscula:
        nueva_cadena += palabra.upper() + ' '
        mayuscula = False
    else:
        nueva_cadena += palabra.lower() + ' '
        mayuscula = True

print(nueva_cadena)

# manera 2:
cadena = str(input("Input: "))

nueva_cadena = ""
# 'hola como estas' .split(' ')
# ['hola', 'como', 'estas']
contador = 0
for palabra in cadena.split(' '):
    if contador % 2 == 0:
        nueva_cadena += palabra.upper() + ' '
        contador += 1
    else:
        nueva_cadena += palabra.lower() + ' '
        contador += 1

print(nueva_cadena)
