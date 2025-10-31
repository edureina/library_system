from library_lib.models import *

def main():
   
   print("......load.......")

   # Recuperar el l'ultim fitxer del Sistema de Biblioteques guardat
   Sistema_cargado = SistemaBibliotecas.cargar_biblioteca("fitxer_biblioteques.pkl")
   #Triadu = Sistema_cargado["Triadu"]
   #Triadu.mostrar_estado_biblio()

   Sistema_cargado.mostrar_estado_sistema()

   #Sistema_cargado.sistema["Triadu"].mostrar_estado_biblio()





# Punto de entrada
if __name__ == "__main__":
    main()

