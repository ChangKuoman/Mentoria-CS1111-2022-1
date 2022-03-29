# print("\033[38;2;28;161;240m" + "BIENVENIDAS Y BIENVENIDOS A UTEC :D" + "\033[0m")

### EJERCICIOS ###

"""
Crear un programa que indique:
Hola mi nombre es <nombre> y mi edad es <edad>
teniendo las variables <nombre> y <edad> como input por el usuario

Comentario Multilinea
"""
# Comentario de una linea

"""
nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))

apellido = input("Ingrese apellido: ")

print("Hola mi nombre es " + nombre + " y mi edad es " + str(edad))
# print("El apellido es " + apellido)

# str( variable )
# int( variable )

print("Hola mi nombre es", nombre, "y mi edad es", edad)

print("Hola mi nombre es {} y mi edad es {}".format(nombre, edad))

# f-string:
print(f"Hola mi nombre es {nombre} y mi edad es {edad}")

# como estas :)
"""

# Pedir al usuario el <año de nacimiento> y determinar la edad en el presente año (2022)

"""
anno_actual = 2022
anno_nacimiento = int(input("Ingrese año de nacimiento: "))
edad = anno_actual - anno_nacimiento

print(f"Su edad en el presente año es: {edad}")

Ingresar el <radio> y la <altura> de un cilindro y hallar el volumen del sólido

import math

radio = float(input("Ingrese radio: "))
altura = float(input("Ingrese altura: "))

volumen = math.pow(math.pi * radio, 2) * altura
# math.pow( base , exponente )

print(f"El volumen del cilindro es {volumen} u^3")

print(math.pi)
print(math.e)
"""

# Pedir al usuario que ingrese una cantidad de <segundos> y el programa
# convierta esa cantidad de segundos a horas, minutos y segundos

cantidad_segundos = int(input("Ingrese segundos: "))

minutos = cantidad_segundos // 60
segundos = cantidad_segundos % 60

horas = minutos // 60
minutos = minutos % 60

# horas:minutos:segundos

print(f"{cantidad_segundos} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")
