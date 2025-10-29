from library_lib.models import *

def main():

    # Llibres
    Sapiens = Libro("Sapiens", "Harari", 2003, True)
    Sapiens.mostrar_info()
    HarryPotter = Libro("Harry Potter", "J.K. Rowling", 2001, True)
    HarryPotter.mostrar_info()
    LODR = Libro("LOFR", "Tolkien", 1968, True)
    LODR.mostrar_info()
    Hobbit = Libro("El Hobbit", "Tolkien", 1957, True)
    Hobbit.mostrar_info()
    CursoIngles = Libro("Curso C2 Ingles", "Klett", 2021, True)
    CursoIngles.mostrar_info()

    # Usuaris
    Edu = Usuario("Eduard", 6, [])
    Cari = Usuario("Carlota", 1, [])
    Marco = Usuario("Marco A", 9, [])
    Olsi = Usuario("Olsi T", 7, [])


    # Biblioteques
    Triadu = Biblioteca("Triadu", [Sapiens], [Edu])
    StuttgiBiblio = Biblioteca("Biblioteca de Stuttgi", [], [])
    BilboAlondiga = Biblioteca("Alondiga Bilbao", [], [])

    print("-----------------------------------------------")
    Triadu.mostrar_estado_biblio()
    print("-----------------------------------------------")

    # Distribuir llibres per les biblioteques
    Triadu.agregar_libro(HarryPotter)
    Triadu.agregar_libro(LODR)
    StuttgiBiblio.agregar_libro(Hobbit)
    BilboAlondiga.agregar_libro(CursoIngles)

    print("-----------------------------------------------")
    Triadu.mostrar_estado_biblio()
    print("-----------------------------------------------")

    # Usuarios se registran en Bibliotecas
    StuttgiBiblio.registrar_usuario(Marco)
    StuttgiBiblio.registrar_usuario(Olsi)
    BilboAlondiga.registrar_usuario(Cari)

    print("-----------------------------------------------")
    Triadu.mostrar_estado_biblio()
    print("-----------------------------------------------")
    
    # Es presten llibres als usuaris
    Triadu.prestar_libro_a_usuario("Sapiens", Edu)
    Triadu.prestar_libro_a_usuario("Sapiens", Edu)
    Triadu.prestar_libro_a_usuario("LODR", Cari)

    print("-----------------------------------------------")
    Edu.mostrar_libros_prestados()
    Cari.mostrar_libros_prestados()
    print("-----------------------------------------------")

    print("-----------------------------------------------")
    print("Total de libros creados", Libro.libros_creados)
    print("Total de bibliotecas creadas", Biblioteca.bibliotecas_creadas)

    # Els usuaris tornen els llibres
    StuttgiBiblio.devolver_libro_de_usuario(Sapiens, Edu)

    print("-----------------------------------------------")
    Triadu.mostrar_estado_biblio()
    StuttgiBiblio.mostrar_estado_biblio()
    print("-----------------------------------------------")

    # Guardar el Sistema de Bibliotecas
    sistema = {
        "Triadu": Triadu,
        "StuttgiBiblio": StuttgiBiblio,
        "BilboAlondiga": BilboAlondiga
    }
    Sistema = SistemaBibliotecas(sistema)
    Sistema.guardar_sistema("fitxer_biblioteques.pkl")



# Punto de entrada
if __name__ == "__main__":
    main()