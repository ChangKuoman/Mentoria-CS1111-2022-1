
### EJERCICIO DE PC ###

"""
2021-2 2.03
1. (5 points) Evalúa estructuras de control selectivas.
Actualmente, uno de los factores mas influyentes para que una persona que se infecta
por Covid-19 se complique es la obesidad, para ello se requiere realizar un programa que
dada la estatura (en centimetros) y el peso (en gramos) de una persona el programa
realice lo siguiente:
• Calcular el IMC = Peso(kg)/(Estatura(m)*Estatura(m))
• Calcule el nivel de peso que le corresponde siguiendo la siguiente tabla:
[   IMC                    Nivel de peso   ]
[   Por debajo de 18.5     Bajo de peso    ]
[   18.5 - 24.9            Normal          ]
[   25.0 - 29.9            Sobrepeso       ]
[   30.0 a más             Obeso           ]

Ingrese el peso ( gramos ): 85000
Ingrese la estatura ( centimetros ): 180
El valor de IMC es: 26.2
Su nivel de peso es: Sobrepeso.

Ingrese el peso ( gramos ): 65000
Ingrese la estatura ( centimetros ): 165
El valor de IMC es: 23.9
Su nivel de peso es: Normal.
"""

from math import pow

peso = int(input("Ingrese peso (en gramos): "))
estatura = int(input("Ingrese estatura (en centímetros): "))

peso = peso / 1000
estatura = estatura / 100

IMC = peso / pow(estatura, 2)
print("El IMC es: ", IMC)

if IMC < 18.5:
    print("Bajo de peso.")
elif IMC < 24.9:
    print("Normal.")
elif IMC < 29.9:
    print("Sobrepeso.")
else:
    print("Obeso.")
