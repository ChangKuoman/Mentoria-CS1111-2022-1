
### EJERCICIO DE PC ###

"""
2021-2 1.02
1. (5 points) Evalúa Diccionarios
Escribe una función que reciba una lista de strings y retorne un diccionario donde la
clave sea la posición correcta de cada palabra según orden alfabético y el valor sea el
string correspondiente.
Algunos ejemplos de diálogo de este programa serían:

input : [ pedro , andres , walter , claudio , alma ]
output : {1: alma, 2: andres , 3: claudio , 4: pedro , 5: walter }
"""

def funcion(lista):
    lista.sort()
    dict = {}
    for i in range(len(lista)):
        dict[i+1] = lista[i]
    return dict

print(funcion(['pedro' , 'andres' , 'walter' , 'claudio' , 'alma']))
