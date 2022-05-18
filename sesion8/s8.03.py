
### EJERCICIO DE PC ###

# factorial de numeros pares hasta el numero que ingresa el usuario (incluyendo)

n = int(input("Ingresar el número: "))
while n < 2:
    n = int(input("Ingresar el número: "))

for numero in range(n, 1, -1):
    if numero % 2 == 0:
        fact = 1
        for i in range(numero, 0, -1):
            fact *= i
        print("El factorial de {} es: {}".format(numero, fact))
        # 6
        # 6! = 6x5x4x3x2x1
