class Artista():
    def __init__(self, nombre, edad, nombre_profesional, estilo):
        self.__nombre=nombre
        self.__edad=edad
        self.__nombre_profesional=nombre_profesional
        self.__estilo=estilo
        self.__musica=False

    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_edad(self,edad):
        self.__edad=edad
    def set_nombre_profesional(self,nombre_profesional):
        self.__nombre_profesional=nombre_profesional
    def set_estilo(self,estilo):
        self.__estilo=estilo
    def set_musica(self, musica):
        self.__musica=musica
    

    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_nombre_profesional(self):
        return self.__nombre_profesional
    def get_estilo(self):
        return self.__estilo
    def get_musica(self):
        return self.__musica


class Musico(Artista):
    def __init__(self, numerocanciones, nombre, edad, nombre_profesional, estilo):
        self.__numerocanciones=numerocanciones
        super().__init__(nombre, edad, nombre_profesional, estilo)
        self.set_musica(True)
        
    def set_numerocanciones(self, numerocanciones):
        self.__numerocanciones=numerocanciones
    def get_numerocanciones(self):
        return self.__numerocanciones


    
def nuevo_artista():
    nombre = input("¿Qué nombre tiene el artista? ")
    edad = input("¿Qué edad tiene el artista? ")
    nombre_profesional = input("¿Qué nombre profesional tiene el artista? ")
    estilo = input("¿Qué estilo tiene el artista? ")
    pregunta = input("¿Es músico?: ")
    if pregunta.lower() == "si":
        numerocanciones = input("¿Cuántas canciones tiene el músico? ")
        miMusico = Musico(numerocanciones, nombre, edad, nombre_profesional, estilo)
        return miMusico
    else:
        miArtista = Artista(nombre, edad, nombre_profesional, estilo)
        return miArtista


