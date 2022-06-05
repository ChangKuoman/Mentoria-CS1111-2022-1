
# enunciado: bucles_anidados_2.JPG

n = int(input("Ingrese n: "))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
