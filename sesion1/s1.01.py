print("\033[38;2;28;161;240m" + "BIENVENIDAS Y BIENVENIDOS A UTEC :D" + "\033[0m")

### EJERCICIO ###

"""
Crear un programa que indique:
Hola mi nombre es <nombre> y mi edad es <edad>
teniendo las variables <nombre> y <edad> como input por el usuario

Comentario Multilinea
"""
# Comentario de una linea


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
