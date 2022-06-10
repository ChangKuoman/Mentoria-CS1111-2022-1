
### EJERCICIO ###

"""
13. Votaciones
Debes crear un programa que permita procesar las votaciones en las elecciones de un
colegio. Se debe leer un número entero N que es el número de votantes. Cada votante
debe escribir el nombre del equipo por quien está votando
• Tu programa debe leer un número entero N que el número votantes
• Tu programa debe analizar las N votaciones para reportar todos los equipos con
sus respectivos votos alcanzados
Consideraciones:
• No usar librerías ni funciones externas
• Debes usar diccionarios de Python para resolver directamente este problema
Algunos ejemplos de diálogo de este programa serían:

Input :
9
Aguilas
Leones
Aguilas
Aguilas
Tigres
Tigres
Halcones
Halcones
Halcones
Output :
Aguilas = 3 votaciones
Halcones = 3 votaciones
Tigres = 2 votaciones
Leones = 1 votacion

Input :
6
Leones
Tigres
Tigres
Tigres
Tigres
Leones
Output :
Leones = 2 votaciones
Tigres = 4 votaciones

Input :
10
Halcones
Leones
Tigres
Halcones
Tigres
Leones
Halcones
Leones
Leones
Leones
Output :
Halcones = 3 votaciones
Leones = 5 votaciones
Tigres = 2 votaciones
"""

n = int(input("Input: "))

votaciones = {}

for i in range(n):
    voto = str(input(""))
    if voto not in votaciones.keys():
        votaciones[voto] = 1
    else:
        votaciones[voto] += 1

print("Output: ")
for key, value in votaciones.items():
    if value == 1:
        print(f"{key} = {value} votacion")
    else:
        print(f"{key} = {value} votaciones")
