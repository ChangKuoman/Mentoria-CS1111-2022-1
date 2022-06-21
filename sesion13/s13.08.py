
### EJERCICIO ###

# recursividad
# 7. (Nivel 1) Recurrencia: Compruebe que la relacion de recurrencia an = an1 + n, con
# valor inicial a0 = 4, es solucion de an = n(n+1)
# 2 + 4. Para ello construya la funcion
# recursiva de la primera expresion y la funcion no-recursiva de la segunda y compruebe
# que ambos resultados son iguales para valores de n desde 1 hasta 10 imprimiendo ambos
# resultados.
# para n=1, an =5 , an =5
# para n=2, an =7 , an =7
# para n=3, an =10 , an =10
# para n=4, an =14 , an =14
# para n=5, an =19 , an =19
# para n=6, an =25 , an =25
# para n=7, an =32 , an =32
# para n=8, an =40 , an =40
# para n=9, an =49 , an =49
# para n=10 , an =59 , an =59

def normal(n):
    return ((n * (n + 1)) / 2) + 4

def recursiva(n):
    if (n == 0):
        return 4
    else:
        return recursiva(n-1) + n

for i in range(1, 11):
    print(f"n={i}, normal={normal(i)}, recursiva={recursiva(i)}")
