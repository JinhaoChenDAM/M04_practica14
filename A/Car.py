class Car:
    #Constructor
    def __init__(self, brand, type, hp, weight):
        self.brand = brand
        self.type = type
        self.hp = hp
        self.weight = weight

    #Getters
    def getBrand(self):
        return self.brand
    def getType (self):
        return self.type
    def getHp (self):
        return self.hp
    def getWeight(self):
        return self.weight

    #Setters
    def setBrand(self, brand):
        self.brand = brand
    def setType(self, type):
        self.type = type
    def setHp(self, hp):
        self.hp = hp
    def setWeight(self, weight):
        self.weight = weight

    #Mètode salutacio()
    def salutacio(self):
        print("Brand: " + self.brand +
              ", Type: " + self.type +
              ", Hp: " + self.hp +
              ", Weight: " + self.weight)

    #Mètode to_dict
    def to_dict(self):
        return{
            "Brand":self.brand,
            "Type":self.type,
            "Hp":self.hp,
            "Weight":self.weight
        }