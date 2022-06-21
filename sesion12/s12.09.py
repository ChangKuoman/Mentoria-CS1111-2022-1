
### INTRODUCCION ###

# archivos
# .json Javascript Object Notation

import json

dict = {
    1: {
    "Nombre": "Pepe",
    "Apellido": "Perez",
    "Edad": 20
    },
    2: {
    "Nombre": "Maria",
    "Apellido": "Juarez",
    "Edad": 21
    },
}

with open("data.json", "w") as file:
    json.dump(dict, file, indent=5)

with open("data.json", "r") as file:
    personas = json.load(file)
    print(json.dumps(personas, indent=5))
