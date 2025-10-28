from library_lib import *

def main():
   
   print(".............")

   # Recuperar el l'ultim fitxer del Sistema de Biblioteques guardat
   Sistema_cargado = SistemaBibliotecas.cargar_biblioteca("fitxer_biblioteques.pkl")
   Triadu = Sistema_cargado["Triadu"]
   BilboAlondiga = Sistema_cargado["BilboAlondiga"]
   StuttgiBiblio = Sistema_cargado["StuttgiBiblio"]

   print("-----------------------------------------------")
   Triadu.mostrar_estado_biblio()
   BilboAlondiga.mostrar_estado_biblio()
   StuttgiBiblio.mostrar_estado_biblio()
   print("-----------------------------------------------")





# Punto de entrada
if __name__ == "__main__":
    main()

