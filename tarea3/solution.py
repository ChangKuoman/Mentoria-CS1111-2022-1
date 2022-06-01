import imageio
import numpy as np

def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta
    de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen.
    Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3
    dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato bmp.
    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))


class Solution:

    def aplicar_negativo(self, lista_3d=leer_imagen('playa (1).bmp')):
        result = list()
        # SU SOLUCION EMPIEZA AQUI
        

        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_corte_circular(self, lista_3d=leer_imagen('playa (1).bmp')):
        result = list()
        # SU SOLUCION EMPIEZA AQUI
       

        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_reflejo_vertical_BGR(self, lista_3d=leer_imagen('playa (1).bmp')):
        result = list()
        # SU SOLUCION EMPIEZA AQUI
        
        
        # SU SOLUCION TERMINA AQUI
        return result

    def aplicar_sepia_modificado(self, lista_3d=leer_imagen('playa (1).bmp')):
        result = list()
        # SU SOLUCION EMPIEZA AQUI
        
          
          
        # SU SOLUCION TERMINA AQUI
        return result

if __name__ == '__main__':
    s = Solution()
    print("Pregunta #1:")
    guardar_imagen('negativo.bmp',s.aplicar_negativo())
    print("Pregunta #2:")
    guardar_imagen('corte_circular.bmp',s.aplicar_corte_circular())
    print("Pregunta #3:")
    guardar_imagen('reflejo_BGR.bmp',s.aplicar_reflejo_vertical_BGR())
    print("Pregunta #4:")
    guardar_imagen('sepia_mod.bmp',s.aplicar_sepia_modificado())