
### EJERCICIO ###

# UTILIZANDO LIST COMPREHENSION
# Teniendo la siguiente cadena, separar cada numero en un elemento de una lista.
cadena = "5,8,6,7,8,6,7"

lista = [int(numero) for numero in cadena.split(",")]
print(lista)
