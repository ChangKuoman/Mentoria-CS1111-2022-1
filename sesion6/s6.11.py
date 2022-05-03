
### EJERCICIO ###

# n = 4
# 1 2 3 4
# 1 2 3
# 1 2
# 1
n = 8

# manera 1
for i in range(1, n+1):
    for j in range(1, n+1-i+1):
        print(j, end="")
    print()

# manera 2
for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j <= n + 1:
            print(j, end="")
    print()
