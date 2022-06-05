
# contar mayusculas

cadena = str(input("Ingrese una cadena: "))

contador_mayusculas = 0
for letra in cadena:
    if letra.isupper():
        contador_mayusculas += 1

print(contador_mayusculas)
