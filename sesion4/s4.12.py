
### EJERCICIO DE PC ###

"""
2021-2 2.03
2. (5 points) Evalúa estructuras de control repetitivas.
Los estudiantes del programa de Ciencia de la Computación de UTEC estan culmi-
nando el semestre 2021 - II, y desean saber su promedio de notasnales. Para ello
necesitan implementar un programa que realice las siguientes tareas.
• Lea una cantidad n >= 1 de cursos.
• Para cada curso deberá ingresar el numero de créditos y la nota correspondiente.
• Para calcular su notafinal, deberá calcular el promedio o media ponderada sigu-
iendo la ecuación:
Prom = (Nota1 * cred1 + Nota2 * cred2 + Nota3 * cred3)/(cred1 + cred2 + cred3)
Para un alumno que solo lleva 3 cursos.

Ingrese cantidad de cursos : 3
Ingrese la nota del curso : 20
Ingrese los creditos del curso : 5
Ingrese la nota del curso : 14
Ingrese los creditos del curso : 4
Ingrese la nota del curso : 16
Ingrese los creditos del curso : 3
Su nota final es: 17.0

Ingrese cantidad de cursos : 2
Ingrese la nota del curso : 15
Ingrese los creditos del curso : 4
Ingrese la nota del curso : 15
Ingrese los creditos del curso : 2
Su nota final es: 15.0

Ingrese cantidad de cursos : 5
Ingrese la nota del curso : 15
Ingrese los creditos del curso : 2
Ingrese la nota del curso : 16
Ingrese los creditos del curso : 3
Ingrese la nota del curso : 14
Ingrese los creditos del curso : 4
Ingrese la nota del curso : 18
Ingrese los creditos del curso : 2
Ingrese la nota del curso : 14
Ingrese los creditos del curso : 1
Su nota final es: 15.3
"""

n_cursos = int(input("Ingrese cantidad de cursos: "))

suma_total = 0
cant_creditos = 0
for i in range(n_cursos):
    nota = int(input("Nota final: "))
    creditos = int(input("Cantidad de creditos: "))
    suma_total += nota * creditos
    cant_creditos += creditos

print(suma_total/cant_creditos)
