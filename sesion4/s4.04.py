
### EJERCICIO ###

# Realizar la suma de la serie armónica.
# f(n) = 1/1 + 1/2 + 1/3 + ... + 1/n

n = int(input("Numero entero: "))
suma = 0
for i in range(1, n+1):
    suma += 1/i
print(round(suma, 2))
