
### EJERCICIO ###

# imprimir todas las vocales de una frase

frase = str(input("Ingrese una frase: "))

for letra in frase:
    # manera 1
    if letra in "aeiouAEIOU":
        print(letra, end=" ")
    # manera 2
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print(letra, end=" ")
