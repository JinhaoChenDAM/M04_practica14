# Clase Cat
class Cat:
    # Constructor de clase Cat
    def __init__(self, breed, color, eyeColor, weight, height, age):
        self.breed = breed
        self.color = color
        self.eyeColor = eyeColor
        self.weight = weight
        self.height = height
        self.age = age

    # Getters y Setters
    def getBreed(self):
        return self.breed

    def setBreed(self, breed):
        self.breed = breed

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getNEyeColor(self):
        return self.eyeColor

    def setNEyeColor(self, eyeColor):
        self.eyeColor = eyeColor

    def getWeight(self):
        return self.Weight

    def setWeight(self, weight):
        self.weight = weight

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age
    # imprime todos los atributos por la pantalla
    def info(self):
        print(f"breed: {self.breed} color: {self.color} eye color: {self.eyeColor} weight: {self.weight} height: {self.height} age: {self.age}")
    # Convierte el objeto a formato dict
    def to_dict(self):
        return {
            "breed": self.breed,
            "color": self.color,
            "eyeColor": self.eyeColor,
            "weight": self.weight,
            "height": self.height,
            "age": self.age
        }

