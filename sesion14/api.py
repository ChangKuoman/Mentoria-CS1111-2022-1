import requests

# api

# .json

nombre = str(input("Ingrese nombre de pokeon: "))

path = "https://pokeapi.co/api/v2/pokemon/" + nombre

respuesta = requests.get(path)

print(respuesta.json())
