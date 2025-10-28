import pickle


class Libro:

    libros_creados = 0

    def __init__(self, titulo: str, autor: str, anio_publicacion: int, disponible: bool):
        if not isinstance(titulo, str):
            raise TypeError("El nombre tiene que ser un String")
        self.titulo = titulo
        if not isinstance(autor, str):
            raise TypeError("El autor tiene que ser un String")
        self.autor = autor
        if not isinstance(anio_publicacion, int):
            raise TypeError("El ano tiene que ser un entero")
        self.anio_publicacion = anio_publicacion
        if not isinstance(disponible, bool):
            raise TypeError("El parametro disponible tiene que ser un boolean")
        self.disponible = disponible
        Libro.libros_creados += 1

    def mostrar_info (self):
        if self.disponible:
            print("Libro:", self.titulo, "; Autor:", self.autor, "; Ano de publicación:", self.anio_publicacion, "; Libro Disponible")
        else:
            print("Libro:", self.titulo, "; Autor:", self.autor, "; Ano de publicación:", self.anio_publicacion, "; Libro Prestado")

    def prestar (self):
        if self.disponible:
            self.disponible = False
            print("Libro %s prestado" % self.titulo)
        else:
            print("Sorry, este libro ya esta siendo usado por otro usuario")

    def devolver (self):
        if self.disponible == False:
            self.disponible = True
            print("Gracias por devolver el libro, esperemos que te haya gustado")
        else:
            print("Lo siento, pero el libro no estaba en tu poder")


class Usuario:

    def __init__(self, nombre: str, id_usuario: int, libros_prestados: list[Libro]):
        if not isinstance(nombre, str):
            raise TypeError("El nombre tiene que ser un String")
        self.nombre = nombre

        if not isinstance(id_usuario, int):
            raise TypeError("El id_usuario tiene que ser un entero")
        self.id_usuario = id_usuario

        for libro in libros_prestados:
            if not isinstance(libro, Libro):
                raise TypeError("Libros_prestados tiene que ser una lista de objetos Libro")
        self.libros_prestados = libros_prestados

    def _prestar_libro(self, libro: Libro):
            self.libros_prestados.append(libro)
            print("El libro %s ha sido prestado al Usuario %s" % (libro.titulo, self.nombre))

    def _devolver_libro(self, libro: Libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print("El libro %s ha sido devuelto" % libro.titulo)
            return True
        else:
            print("El libro no estaba prestado a %s" % self.nombre)
            return False

    def mostrar_libros_prestados(self):
        print("Los siguientes libros han sido prestados a %s: " % self.nombre)
        for libro in self.libros_prestados:
            libro.mostrar_info()




class Biblioteca:

    bibliotecas_creadas = 0
    usuarios = []
    libros_sistema = []

    def __init__(self, nombre, libros: list[Libro], usuarios: list[Usuario]):

        Biblioteca.bibliotecas_creadas += 1

        if not isinstance(nombre, str):
            raise TypeError("El nombre de la biblioteca tiene que ser un String")
        self.nombre = nombre

        for libro in libros:
            if not isinstance(libro, Libro):
                raise TypeError("libros tiene que ser una lista de objetos Libro")
        self.libros_biblio = libros
        Biblioteca.libros_sistema.extend(libros)
        print(Biblioteca.libros_sistema)
        
        for usuario in usuarios:
            if not isinstance(usuario, Usuario):
                raise TypeError("usuarios tiene que ser una lista de objetos Usuario")
            if usuario not in Biblioteca.usuarios:
                Biblioteca.usuarios.append(usuario)



    def agregar_libro(self, libro):
        self.libros_biblio.append(libro)
        Biblioteca.libros_sistema.append(libro)
        print("El libro: %s ha sido agregado a la biblioteca: %s" % (libro.titulo, self.nombre))

    def registrar_usuario(self, usuario):
        if usuario not in Biblioteca.usuarios:
            Biblioteca.usuarios.append(usuario)
            print("El usuario %s ha sido registrado en el sistema de bibliotecas" % usuario.nombre)
        else:
            print("El usuario %s ya estaba en el registro." % usuario.nombre)

    def prestar_libro_a_usuario(self, titulo_libro:str , usuario: Usuario):
        # TODO: Buscar el llibre en totes les biblioteques i imprimir un missatge de que el llibre esta disponible
        #       en una altre biblioteca in case.
        libro_buscado = next( (libro for libro in Biblioteca.libros_sistema if libro.titulo == titulo_libro), None) 
        if libro_buscado != None:
            if libro_buscado.disponible:
                usuario._prestar_libro(libro_buscado)
                libro_buscado.prestar()
                self.libros_biblio.remove(libro_buscado)
            else:
                print("El libro %s ya esta siendo usado por otro usuario" % libro_buscado.titulo)
        else:
            print("Lo sentimos, el libro buscado no esta disponible en esta biblioteca")
        
    def devolver_libro_de_usuario(self, libro: Libro, usuario: Usuario):
        if usuario._devolver_libro(libro):
            self.libros_biblio.append(libro)

    def mostrar_estado_biblio(self):
        print(f"Los siguientes libros estan disponibles en la biblioteca: {self.nombre}")
        for libro in self.libros_biblio:
            libro.mostrar_info()
        print("Los siguientes usuarios han sido registrados en el sistema de bibliotecas publicas: ") 
        for usuario in Biblioteca.usuarios:
            print(usuario.nombre)

    def mostrar_estado_sistema(self):
        print("El Sistema de Bibliotecas contiene los siguientes títulos")
        for libro in Biblioteca.libros_sistema:
            libro.mostrar_info()
        print("Los siguientes usuarios han sido registrados en el sistema de bibliotecas publicas: ") 
        for usuario in Biblioteca.usuarios:
            print(usuario.nombre)


class SistemaBibliotecas:

    def __init__(self, sistema: dict):
        if not isinstance(sistema, dict):
            raise TypeError("sistema tiene que ser un diccionario de objetos tipo Libreria")
        self.sistema = sistema


    def guardar_sistema(self, nombre_archivo: str):
        with open(nombre_archivo, "wb") as f:
            pickle.dump(self.sistema, f)
            print(f"El Sistema de Bibliotecas ha sido guardado en {nombre_archivo}")


    @staticmethod
    def cargar_biblioteca(nombre_archivo: str) -> dict:
        with open(nombre_archivo, "rb") as f:
            sistema = pickle.load(f)
            if sistema is not None:
                print(f"El Sistema de Bibliotecas ha sido cargado desde {nombre_archivo}")
            return sistema

