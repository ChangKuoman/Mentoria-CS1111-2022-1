
### EJERCICIO ###

# n = 5
# * * * * *
#       *
#     *
#   *
# * * * * *

n = 6
for i in range(n):
    for j in range(n):
        if i == 0 or i +1 == n or i + j == n -1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
