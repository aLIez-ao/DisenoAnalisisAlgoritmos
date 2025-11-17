from algoritmos import *
from runner import *
from utils import *

if __name__ == "__main__":

    # -------------------------------
    # Generar datos de prueba
    # -------------------------------

    
    # -------------------------------
    # Diccionario de funciones
    # -------------------------------
    funciones = {
        # Algoritmos dinámicos
        #"laberinto": lambda: run_resolver_laberinto(laberinto),
    }

    # -------------------------------
    # Ejecutar algoritmo elegido
    # -------------------------------
    algoritmo_ejecutar = "laberinto"
    funciones[algoritmo_ejecutar]()
