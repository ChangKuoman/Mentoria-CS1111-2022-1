
### INTRODUCCION ###

# diccionarios
dict = {
    "llave": "valor",
    "llave2": "valor",
    1:48
}

print(dict[1])

dict.pop("llave")
del dict["llave2"]

print(dict)

dict.clear()

print(dict)

del dict
print(dict)
