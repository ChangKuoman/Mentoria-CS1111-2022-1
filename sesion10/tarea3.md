
# Consideraciones para la tarea2

## 1. Aplicar Negativo
``` python
def aplicar_negativo(self, lista_3d=leer_imagen('playa (1).bmp')):
    result = list()
    # SU SOLUCION EMPIEZA AQUI
    result = lista_3d[::]
    for fila in range(len(lista_3d)):
        for columna in range(len(lista_3d[fila])):
            result[fila][columna][0] = # aqui pintar rojo
            result[fila][columna][1] = # aqui pintar verde
            result[fila][columna][2] = # aqui pintar azul

    # SU SOLUCION TERMINA AQUI
    return result
```
## 2. Aplicar Corte Circular
``` python
def aplicar_corte_circular(self, lista_3d=leer_imagen('playa (1).bmp')):
    result = list()
    # SU SOLUCION EMPIEZA AQUI
    h = len(lista_3d)
    Cx = len(lista_3d[0])//2
    Cy = h//2
    # for anidado
    if condicion: # la condición es la fórmula del circulo
        # aqui pintar original
    else:
        # aqui pintar negro

    # SU SOLUCION TERMINA AQUI
    return result
```
