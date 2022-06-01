
### INTRODUCCION ###

# diccionarios

# llave -> valor
# llave es tipo de dato inmutable
# valor es tipo de datos inmutable o mutable
# key -> value
# hola -> hola es palabra para saludar
# mesa -> 4 patas y un algo

colores = {
    "rojo":"red",
    "azul":"ble"
}

colores["azul"] = "blue"

for llave in colores.keys():
    print(llave, "+", colores[llave])
print("----")
for valor in colores.values():
    print(valor)
print("----")
for llave, valor in colores.items():
    print(llave, "+", valor)
