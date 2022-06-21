
### EJERCICIO ###

# recursividad
# 6. (Nivel 1) Usando recursividad desarrollar un programa en Python que pida un numero y
# encuentre la suma de los enteros positivos pares desde 2 hasta N. Validar N; si es impar,
# mostrar un mensaje de ERROR:
# Ejemplo:
# Ingrese numero : 5
# ERROR
# Ingrese numero : 6
# Respuesta : 12

def hallar_suma(n):
    if (n == 2):
        return 2
    else:
        return n + hallar_suma(n - 2)

n = int(input("Ingrese numero: "))
if (n % 2 != 0):
    print("ERROR")
else:
    print(hallar_suma(n))
