
### EJERCICIO DE PC ###

"""
2020-2 1.09
2. (5 points) Cuenta la leyenda que a cada persona, según el día y mes en que nació le
corresponde una piedra preciosa, según esta tabla:
[   Mes                                      |  Día Par   |  Día Impar   ]
[   Enero, Febrero, Marzo, Abril             |  Esmeralda |  Zaro        ]
[   Mayo, Junio, Julio, Agosto               |  Rubí      |  Topacio     ]
[   Setiembre, Octubre, Noviembre, Diciembre |  Amatista  |  Jade        ]
Desarrolle e implemente un programa que permita determinar la piedra preciosa que le
corresponde a "n" personas.
• De cada persona se leerá el día y el nombre del mes en que nació. Trabaje bajo
el supuesto que los valores del día y mes corresponden a una fecha correcta. (No
tiene que vericar el dato)
• Se pide expresamente que implemente una función llamada hallaPiedra, que
reciba como parámetro el día y el mes y la función devuelva una cadena con el
nombre de la piedra preciosa.

Numero de personas : 3
Persona numero : 1
Dia : 30
Mes : Setiembre
Su piedra preciosa es Amatista
Persona numero : 2
Dia : 4
Mes : Enero
Su piedra preciosa es Esmeralda
Persona numero : 3
Dia : 23
Mes : Octubre
Su piedra preciosa es Jade
Chao !

Numero de personas : 2
Persona numero : 1
Dia : 14
Mes : Mayo
Su piedra preciosa es Rubi
Persona numero : 2
Dia : 20
Mes : Febrero
Su piedra preciosa es Esmeralda
Chao !
"""

def hallaPiedra(dia, mes):
    if mes in ['enero', 'febrero', 'marzo', 'abril']:
        if dia % 2 == 0:
            return "Esmeralda"
        else:
            return "Zaro"
    elif mes in ['mayo', 'junio', 'julio', 'agosto']:
        if dia % 2 == 0:
            return "Rubí"
        else:
            return "Topacio"
    elif mes in ['setiembre', 'octubre', 'noviembre', 'diciembre']:
        if dia % 2 == 0:
            return "Amatista"
        else:
            return "Jade"

n = int(input("Ingrese cantidad de personas: "))
for i in range(n):
    print(f"Persona numero {i+1}")
    dia = int(input("Ingrese día: "))
    mes = str(input("Ingrese mes:")).lower()
    print(f"Su piedra preciosa es {hallaPiedra(dia, mes)}")

print("chao!")
