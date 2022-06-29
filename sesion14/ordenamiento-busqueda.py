
# ordenamiento y busqueda
# ordenamos las peliculas por anio, ingresamos un anio y
# por busqueda binario buscamos e imprimimos el nombre de la pelicula

peliculas = [
    {'anio': 2010, 'nombre': 'Persona1'},
    {'anio': 2013, 'nombre': 'Persona4'},
    {'anio': 2014, 'nombre': 'Persona5'},
    {'anio': 2012, 'nombre': 'Persona3'},
    {'anio': 2015, 'nombre': 'Persona6'},
    {'anio': 2011, 'nombre': 'Persona2'}
]

def ordenar(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j]['anio'] > lista[j + 1]['anio']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def binaria(lista, elem):

    if len(lista) == 1:
        if lista[0]['anio'] == elem:
            return lista[0]
        else:
            return None

    n = len(lista)
    mitad = n//2
    if lista[mitad]['anio'] == elem:
        return lista[mitad]

    elif lista[mitad]['anio'] < elem:
        return binaria(lista[mitad:], elem)
    elif lista[mitad]['anio'] > elem:
        return binaria(lista[:mitad], elem)

anio_buscado = 2014
ordenar(peliculas)
print(*peliculas)
valor = binaria(peliculas, anio_buscado)
if valor is not None:
    print(valor['nombre'])
