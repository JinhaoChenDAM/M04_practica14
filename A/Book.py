class Book:
    # Creem el constructor amb els seus atributs
    def __init__ (self, nom, autor, any, tapa, idioma, genere):
        self.nom = nom
        self.autor = autor
        self.any = any
        self.tapa = tapa
        self.idioma = idioma
        self.genere = genere

    # Afegim els Getters/Setters
    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getAny(self):
        return self.any

    def setAny(self, any):
        self.any = any

    def getTapa(self):
        return self.tapa

    def setTapa(self, tapa):
        self.tapa = tapa

    def getIdioma(self):
        return self.idioma

    def setIdioma(self, idioma):
        self.idioma = idioma

    def getGenere(self):
        return self.genere

    def setGenere(self, genere):
        self.genere = genere

    # Creem una funció que imprimeix els atributs de l'objecte per pantalla
    def info(self):
        print("El llibre titolat {nom} escrit per {autor} en l'any {any} de gènere"
              " de {genere} ha publicat un llibre de tapa {tapa}"
              " en {idioma}".format(nom=self.nom, autor=self.autor, any=self.any,
                                    genere=self.genere, tapa=self.tapa, idioma=self.idioma))

    #Mètode to_dict()
    def to_dict(self):
        return{
            "Nom":self.nom,
            "Autor":self.autor,
            "Any":self.any,
            "Genere":self.genere,
            "Tapa":self.tapa,
            "Idioma":self.idioma
        }