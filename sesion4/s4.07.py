
### EJERCICIO ###

# Pedir al usuario un número entero y validar que se encuentre del 1 al 12 (inclusive)
# Luego imprimir la tabla de multiplicar en el formato indicado
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 8 x 10 = 80
# 8 x 11 = 88
# 8 x 12 = 96

n = int(input("Numero: "))
while n <= 0 or n >= 13:
    n = int(input("Numero: "))

for i in range(1, 13, 1):
    print(f"{n} x {i} = {n*i}") # f-string
