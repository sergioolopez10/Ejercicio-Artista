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


    
def nuevo_artista(lista_artistas):
    try:
        nombre = input("¿Qué nombre tiene el artista? ")
        edad = input("¿Qué edad tiene el artista? ")
        nombre_profesional = input("¿Qué nombre profesional tiene el artista? ")
        estilo = input("¿Qué estilo tiene el artista? ")
        pregunta = input("¿Es músico?: ")
        if pregunta.lower() == "si":
            numerocanciones = input("¿Cuántas canciones tiene el músico? ")
            miMusico = Musico(numerocanciones, nombre, edad, nombre_profesional, estilo)
            lista_artistas.append(miMusico)
            return miMusico
        if pregunta.lower() == "no":
            miArtista = Artista(nombre, edad, nombre_profesional, estilo)
            lista_artistas.append(miArtista)
            return miArtista
        else:
            print ("Por favor, introduzca sólo sí o no")
    except ValueError:
        print("La edad y el número de canciones deben ser números enteros.")


def finalizar_programa():
    print("El programa se ha finalizado")

def modificar_artista(lista_artistas):
    if not lista_artistas:
        print("No hay artistas en la lista")
        return
    
    nombre_artista = input("Ingrese el nombre del artista que desea modificar: ")
    for artista in lista_artistas:
        if artista.get_nombre() == nombre_artista:
            print("Datos actuales del artista:")
            print(f"Nombre: {artista.get_nombre()}")
            print(f"Edad: {artista.get_edad()}")
            print(f"Nombre profesional: {artista.get_nombre_profesional()}")
            print(f"Estilo: {artista.get_estilo()}")
            if isinstance(artista, Musico):
                print(f"Número de canciones: {artista.get_numerocanciones()}")

            numerocanciones = None
            
            nombre = input("Ingrese el nuevo nombre del artista: ")
            edad = input("Ingrese la nueva edad del artista: ")
            nombre_profesional = input("Ingrese el nuevo nombre profesional del artista: ")
            estilo = input("Ingrese el nuevo estilo del artista: ")
            if isinstance(artista, Musico):
                try:
                    numerocanciones = input("Ingrese el nuevo número de canciones: ")
                    artista.set_numerocanciones(numerocanciones)
                except ValueError:
                    print("El número de canciones debe ser un número entero.")
            artista.set_nombre(nombre)
            artista.set_edad(edad)
            artista.set_nombre_profesional(nombre_profesional)
            artista.set_estilo(estilo)

            print("Artista modificado con éxito.")
            print("Lista de artistas actualizada:")
            for artista in lista_artistas:
                if isinstance(artista, Musico):
                    print(f"Nombre del músico: {artista.get_nombre()}, Edad del músico: {artista.get_edad()}, Nombre profesional del músico: {artista.get_nombre_profesional()}, Estilo del músico: {artista.get_estilo()}, Número de canciones que tiene: {artista.get_numerocanciones()}")
                else:
                    print(f"Nombre del artista: {artista.get_nombre()}, Edad del artista: {artista.get_edad()}, Nombre profesional del artista: {artista.get_nombre_profesional()}, Estilo del artista: {artista.get_estilo()}")
        else:
            print("No se encontró un artista con ese nombre.")


def eliminar_artista(lista_artistas):
    if not lista_artistas:
        print("No hay artistas en la lista")
        return
    nombre_artista = input("Ingrese el nombre del artista que desea eliminar: ")
    encontrado=False
    for i, artista in enumerate(lista_artistas):
        if artista.get_nombre() == nombre_artista:
            del lista_artistas[i]
            print("Artista eliminado con éxito.")
            print("Lista de artistas actualizada:")
            encontrado=True
            for artista in lista_artistas:
                if isinstance(artista, Musico):
                    print(f"Nombre del músico: {artista.get_nombre()}, Edad del músico: {artista.get_edad()}, Nombre profesional del músico: {artista.get_nombre_profesional()}, Estilo del músico: {artista.get_estilo()}, Número de canciones que tiene: {artista.get_numerocanciones()}")
                else:
                    print(f"Nombre del artista: {artista.get_nombre()}, Edad del artista: {artista.get_edad()}, Nombre profesional del artista: {artista.get_nombre_profesional()}, Estilo del artista: {artista.get_estilo()}")
    if not encontrado: 
        print("No hay ningún artista con ese nombre")



def main():
    lista_artistas = []

    while True:
        try:
            P=int(input("Si desea añadir un artista:1. Si desea modificar un artista:2. Si desea eliminar un artista:3 Si desea finalizar el programa:4 "))
            if P==1:
                nuevo_artista(lista_artistas)
            if P==2:
                modificar_artista(lista_artistas)
            if P==3:
                eliminar_artista(lista_artistas)
            if P==4:
                finalizar_programa()
                break
            else:
                print("Por favor, introduza un número entre 1 y 4 en función de lo que desee hacer.")
        except ValueError:
            print("Por favor, introduzca un número entre 1 y 4 en función de lo que desee hacer.")


if __name__=='__main__':
    main()
