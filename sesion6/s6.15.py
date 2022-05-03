
### EJERCICIO ###

# Implemente un programa que permita leer
# un número entero mayor a 50 y el programa imprima numeros desde el 1
# hasta el numero que se ha ingresado como dato. El programa debe
# imprimir diez números por línea, cada número se imprime en un ancho de 5 lugares.


numero = int(input("numero: "))
while numero < 50:
    numero = int(input("numero: "))

contador = 0
for i in range(1, numero+1):
    print("{:5}".format(i), end="")
    contador += 1
    if contador == 10:
        print()
        contador = 0
