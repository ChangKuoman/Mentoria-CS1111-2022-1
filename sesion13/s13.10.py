
### EJERCICIO ###

# recursividad
# 10. (Nivel 2) Escribir una funcion recursiva que reciba como input dos numeros y devuelva
# como resultado la multiplicacion de todos los numeros desde el inicio del rango (numero
# menor) hasta elnal del rango (numero mayor).
# Ejemplos:
# Ingrese un numero : 30
# Ingrese un numero : 35
# Resultado : 1168675200
# Ingrese un numero : 27
# Ingrese un numero : 25
# Resultado : 17550
#              num1 < num2
def multiplicar(num1, num2):
    if (num1 == num2):
        return num1
    else:
        return num1 * multiplicar(num1 + 1, num2)

print(multiplicar(30, 35))
print(multiplicar(25, 27))
