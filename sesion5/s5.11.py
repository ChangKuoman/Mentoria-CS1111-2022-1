
# functions

nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))


def imprimir_nombre(nombre, edad):
    print(f"EL NOMBRE ES: {nombre}")

    print("la edad es: {}".format(edad))
    print("la edad es: " + str(edad))
    print("la edad es: %d" % edad)
    print(f"la edad es: {edad}")
    print("la edad es:", edad)


# llamar a la funcion despues de definirla
imprimir_nombre("MARIA", 18)
imprimir_nombre("PEPITO", 17)
imprimir_nombre(nombre, edad)
