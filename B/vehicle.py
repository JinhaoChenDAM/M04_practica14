# Classe Vehicle
class Vehicle:
    # Constructor de classe Vehicle
    def __init__(self, tipo, marca, color, largo, ancho, alto):
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    # Getters y Setters
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getLargo(self):
        return self.largo

    def setLargo(self, largo):
        self.largo = largo

    def getAncho(self):
        return self.ancho

    def setAncho(self, ancho):
        self.ancho = ancho

    def getAlto(self):
        return self.alto

    def setAlto(self, alto):
        self.alto = alto

    # Imprime todos los attributos por la pantalla
    def parts(self):
        print(
            "vehiculo es un {tipo} de color {color} y de marca {marca}, mide {largo}cm de largo, {ancho}cm de ancho y {alto}cm de alto"
            .format(tipo=self.tipo, color=self.color, marca=self.marca, largo=self.largo, ancho=self.ancho,
                    alto=self.alto))

    # Convierte el objeto a formato dict
    def to_dict(self):
        return {
            "tipo": self.tipo,
            "color": self.color,
            "marca": self.marca,
            "largo": self.largo,
            "ancho": self.ancho,
            "alto": self.alto
        }
