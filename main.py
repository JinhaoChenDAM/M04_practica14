import json

from B.Cat import Cat
from B.vehicle import Vehicle

# Crear la lista de cats con 5 instancias
cats = [
    Cat("Shorthair","black","black", 10,30,3),
    Cat("Wirehair","white","black", 15,30,2),
    Cat("Birman","white","blue", 13,35,5),
    Cat("Bengal","brown","black", 12,40,10),
    Cat("Bombay","yellow","brown", 14,20,7)
]
# Crear la lista de vehicles con 5 instancias
vehicles = [
    Vehicle("coche", "Tesla", "blanco", 400, 180, 160),
    Vehicle("moto", "Honda", "azul", 160, 50, 80),
    Vehicle("moto", "Hyundai", "negro", 165, 53, 78),
    Vehicle("moto", "Toyota", "azul", 155, 52, 78),
    Vehicle("coche", "Nissan", "blanco", 370, 170, 170)
]
# Convertir las 2 listas de objectos a una lista de diccionario
cats_list = [c.to_dict() for c in cats]
vehicles_list = [v.to_dict() for v in vehicles]

# Guardarlas en un contenidor
data = {"cats":cats_list,"vehicles":vehicles_list}

# Crear el archivo cats.json con el contenidor
with open("json_API/cats.json", 'w') as file:
    json.dump(data,file)