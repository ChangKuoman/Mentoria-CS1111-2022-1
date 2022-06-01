import imageio
import numpy as np

def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen. Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d

def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3 dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato bmp.
    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))

class Solution:
    def aplicar_escala_de_grises(self, lista_3d = leer_imagen('foto_utec.bmp')):
        result = lista_3d[::]
        # SU SOLUCION EMPIEZA AQUI
        for fila in range(len(lista_3d)):
            for columna in range(len(lista_3d[fila])):
                gris = (sum(lista_3d[fila][columna]))//3
                result[fila][columna][0] = gris
                result[fila][columna][1] = gris
                result[fila][columna][2] = gris

        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_sepia(self, lista_3d = leer_imagen('foto_utec.bmp')):
        result = lista_3d[::]
        # SU SOLUCION EMPIEZA AQUI
        for fila in range(len(lista_3d)):
            for columna in range(len(lista_3d[fila])):
                sepiaRojo = 0.393 * lista_3d[fila][columna][0] + 0.769 * lista_3d[fila][columna][1] + 0.189 * lista_3d[fila][columna][2]
                if sepiaRojo > 255:
                    sepiaRojo = 255
                sepiaRojo = round(sepiaRojo)
                result[fila][columna][0] = sepiaRojo

                sepiaVerde = 0.349 * lista_3d[fila][columna][0] + 0.686 * lista_3d[fila][columna][1] + 0.168 * lista_3d[fila][columna][2]
                if sepiaVerde > 255:
                    sepiaVerde = 255
                sepiaVerde = round(sepiaVerde)
                result[fila][columna][1] = sepiaVerde

                sepiaAzul = 0.272 * lista_3d[fila][columna][0] + 0.534 * lista_3d[fila][columna][1] + 0.131 * lista_3d[fila][columna][2]
                if sepiaAzul > 255:
                    sepiaAzul = 255
                sepiaAzul = round(sepiaAzul)
                result[fila][columna][2] = sepiaAzul

        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_reflejo_horizontal(self, lista_3d = leer_imagen('foto_utec.bmp')):
        result = lista_3d[::]
        # SU SOLUCION EMPIEZA AQUI
        # for fila in range(len(lista_3d)):
        #     result[fila] = lista_3d[fila][::-1]

        result = lista_3d[::-1]

        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_marco(self, lista_3d = leer_imagen('foto_utec.bmp')):
        result = lista_3d[::]
        # SU SOLUCION EMPIEZA AQUI
        for fila in range(len(lista_3d)):
            for columna in range(len(lista_3d[fila])):
                if fila < len(lista_3d)//5:
                    result[fila][columna] = [0, 0, 0]
                else:
                    result[fila][columna] = lista_3d[fila][columna]
        # SU SOLUCION TERMINA AQUI
        return result

result = Solution.aplicar_escala_de_grises('foto_utec.bmp')
guardar_imagen('foto_gris.bmp', result)
result = Solution.aplicar_sepia('foto_utec.bmp')
guardar_imagen('foto_sepia.bmp', result)
result = Solution.aplicar_reflejo_horizontal('foto_utec.bmp')
guardar_imagen('foto_inversa_2.bmp', result)
result = Solution.aplicar_marco('foto_utec.bmp')
guardar_imagen('foto_marco.bmp', result)
