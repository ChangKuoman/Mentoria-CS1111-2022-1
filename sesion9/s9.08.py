
### INTRODUCCION ###

# imagenes
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# leyendo la imagen
image = Image.open("dog.jpg")
matrix = np.array(image, dtype='int')

# modificando la imagen
def modificar(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < len(matrix)/2:
                matrix[i][j][0] = 0
            else:
                matrix[i][j][1] = 0

modificar(matrix)

# mostrando la imagen
plt.imshow(matrix[::])
plt.show()
