
### EJERCICIO ###

# Escribir un programa que reciba un número de DNI y usando una función verifique e imprima si es válido
# (tener una longitud de 8 dígitos) o no.

def verifica_dni(dni):
    # int
    if 9_999_999 < dni < 100_000_000:
        return True
    else:
        return False
    # string
    if len(dni) == 8:
        return True
    else:
        return False

# print(verifica_dni("85412367"))
# print(verifica_dni("8541236785"))
# print(verifica_dni(85412367))
# print(verifica_dni(85412367845))
