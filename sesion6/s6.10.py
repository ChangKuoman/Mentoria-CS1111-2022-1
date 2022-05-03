
### EJERCICIO ###

# n = 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# manera 1
n = 8
i = 1
while i <= n:
    j = 1
    fila = " "
    while j <= i:
        fila += str(j)
        j += 1
    print(fila)
    i += 1

# manera 2
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
