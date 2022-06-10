
### INTRODUCCION ###

# diccionarios anidados
personas = {
    "12345678": {
        "nombre": "Pepe",
        "apellido": "Perez",
        "telefonos": [987654321, 987654322]
    },
    "87654321": {
        "nombre": "Pepe",
        "apellido": "Perez"
    }
}

print(personas["12345678"]["telefonos"][0])
