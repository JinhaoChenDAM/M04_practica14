import json

from A.Book import Book
from A.Car import Car
from B.Cat import Cat
from B.vehicle import Vehicle

# 5 Books
books = [
    Book("Flors per a l'algernon", "Mike", 2004, "Dura", "Català", "Ciència Ficció"),
    Book("Tom&Jerry", "Olagon", 1892, "dura", "Anglès", "Cartoon"),
    Book("Lucky Luke", "Boing", 1921, "Blanda", "Castellà", "Cartoon"),
    Book("Bob Esponja", "David", 2006, "Blanda", "Francés", "Terror"),
    Book("HarryPotter", "Logan", 1989, "Dura", "Anglès", "Comedia")
]

# 5 Cars
cars = [
    Car("Honda", "Drift", 1090, 890),
    Car("Hyundai", "Offroad", 270, 1800),
    Car("Nissan", "Race", 890, 590),
    Car("Mitsubishi", "Offroad", 480, 780),
    Car("Ferrari", "Drift", 780, 430)
]

# Convertim les dues llistes del pas 2 en llistes de diccionaris utilitzant el mètode to_dict().
books_list = [b.to_dict() for b in books]
cars_list = [c.to_dict() for c in cars]

#Guardem les dues llistes del pas 3 en un objecte contenidor.
dades = {"books":books_list,"cars":cars_list}

#Guardem l’objecte contenidor del 3er pas en un arxiu en format .json (open())
with open("json_API/booksAndCars.json", "w") as file:
    json.dump(dades,file)


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