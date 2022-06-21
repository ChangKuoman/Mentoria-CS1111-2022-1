
### EJERCICIO ###

# recursividad
# 8. (Nivel 2) Python dispone de una serie de funciones integradas al lenguaje, y tambien
# permite crear funciones denidas por el usuario para ser usadas en su propios programas.
# La funcion len(variable) de phyton devuelve la longitud de una cadena de caracteres
# o el numero de elementos de una lista.
# Escribe un programa que realice los siguiente:
#  Solicita al usuario ingresar una cadena de caracteres.
#  Obtiene la longitud de la cadena
#  Imprime la longitud de la cadena.
# Para obtener la longitud de la cadena, implemente y use la siguiente funcion recursiva
# (imitando la funcion len):
#  obt longitud recibe como parametro una cadena y retorna la longitud de la cadena.
# Algunos ejemplos de dialogo de este programa serian:
# Ingrese una cadena : El cielo es azul
# La longitud de la cadena es: 16
# Ingrese una cadena : Hasta el infinito y mas alla
# La longitud de la cadena es: 28

def obj_longitud(cadena):
    # caso  base
    if (cadena == ''):
        return 0
    # llamada recursiva
    else:
        return 1 + obj_longitud(cadena[1::])

print(obj_longitud("El cielo es azul"))
print(obj_longitud("Hasta el infinito y mas alla"))
