
### INTRODUCCION ###

# imagenes
import matplotlib.pyplot as plt

matriz = [
    [[255, 0, 0], [255, 255, 255], [255, 0, 0],[255, 0, 0], [255, 255, 255], [255, 0, 0]],
    [[100, 0, 251], [0, 55, 55], [255, 0, 0],[255, 0, 0], [255, 255, 255], [255, 0, 0]],
]
# RGB
# RED-GREEN-BLUE

# modificando la imagen
def modificar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j][0] = 100
            matriz[i][j][1] = 0
            matriz[i][j][2] = 100

# modificar(matriz)

# mostrando la imagen
plt.imshow(matriz[::])
plt.show()
