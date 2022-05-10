
### EJERCICIO ###

# Escribir un programa que pida numeros positivos al usuario. Mostrar el numero cuya sumatoria de digitos
# fue mayor y la cantidad de numeros cuya sumatoria de digitos fue menor que 10. Utilizar una o mas
# funciones, segun sea necesario.

# n numeros
# 485 => 4 + 8 + 5 = 17
# 356 => 3 + 5 + 6 = 14
# 33 => 3 + 3 = 6

def hallar_suma_digitos(numero):
    # for each
    numero = str(numero)
    suma = 0
    for digito in numero:
        suma += int(digito)
    # for con indices
    numero = str(numero)
    suma2 = 0
    for i in range(len(numero)):
        suma2 += int(numero[i])
    return suma2

cantidad = 0
suma_digitos_mayor = 0
elemento_mayor = 0
# n = int(input("Ingrese n: "))
for i in range(n):
    num = int(input("Numero: "))
    suma_digitos = hallar_suma_digitos(num)

    if suma_digitos < 10:
        cantidad += 1

    if suma_digitos > suma_digitos_mayor:
        suma_digitos_mayor = suma_digitos
        elemento_mayor = num

print("El numero con mayor suma de digitos es: %d" % elemento_mayor)
print("La cantidad de numeros con suma menor que 10 es %d" % cantidad)
