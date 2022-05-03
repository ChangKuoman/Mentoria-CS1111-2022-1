
### EJERCICIO DE PC ###

"""
Deberas crear una funcion que se llame maravilla. Esta función recibira 3 parametros, y tendra las siguientes caracteristicas:
• El primer parametro sera un caracter, el cual puede ser alguno de estos simbolos:
”+” (mas) ”-” (menos) ”*” (por) ”/” (entre) .
• El segundo y el tecer parametros seran dos numeros enteros .
• La funcion devolvera el resultado de la operacion enviada.
• Si el primer parametro fuera ”entre” y el segundo numero un cero, debera imprimir un mensaje de error y no devolvera nada.
"""

def maravilla(caracter, n1, n2):
    if caracter == "+":
        return n1 + n2
    elif caracter == "-":
        return n1 - n2
    elif caracter == "*":
        return n1 * n2
    elif caracter == "/":
        if n2 == 0:
            return "no se puede dividir entre 0"
        else:
            return n1 / n2
    else:
        return "caracter invalido"


print(maravilla("+", 5, 8))
print(maravilla("-", 5, 8))
print(maravilla("*", 5, 8))
print(maravilla("/", 5, 8))
print(maravilla("a", 5, 8))
print(maravilla("/", 5, 0))
