
### EJERCICIO ###

# hallar cuantas A en en genoma
genoma = "SKDJFNSDAAKJKFKN"
print(len(genoma))
contador = 0
for letra in genoma:
    if letra == "A":
        contador += 1
print(contador)
