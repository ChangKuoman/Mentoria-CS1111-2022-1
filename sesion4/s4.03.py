
### EJERCICIO ###

# Imprimir el resultado de la suma de los números de 1 a <n> utilizando un for

n = int(input("Numero entero: "))
suma = 0
for i in range(n+1):
    suma += i
    # suma = suma + i
print(suma)
