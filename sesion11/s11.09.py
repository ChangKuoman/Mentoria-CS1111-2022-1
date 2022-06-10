
### EJERCICIO DE PC ###

"""
3. (5 points) Evalúa Diccionarios.
Escribe una función que reciba 2 diccionarios y retorne un diccionario con la unión
de ellos. La unión de dos diccionarios inserta un valor si la misma llave y clave se
encuentra en ambos diccionarios.
Algunos ejemplos de diálogo de este programa serían:

Input : {’a’:1, ’b’:2, ’c’:3} {’a’:1, ’d’:2, ’c’:4} Output : {’a’:1}
"""

def union(dict1, dict2):
    dict_union = {}
    for key in dict1.keys():
        if key in dict2.keys():
            if dict1[key] == dict2[key]:
                dict_union[key] = dict1[key]
    return dict_union

print(union({'a':1, 'b':2, 'c':3}, {'a':1, 'd':2, 'c':4}))
