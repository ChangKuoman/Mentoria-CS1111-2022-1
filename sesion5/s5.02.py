
### EJERCICIO ###

# X
# X X
# X X X
# X X X X
# X X X X X

n = int(input("Ingrese n: "))

for i in range(1, n):
    for j in range(i):
        print("X", end=" ")
    print()
