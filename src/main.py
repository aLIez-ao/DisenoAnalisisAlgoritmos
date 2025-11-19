from algoritmos import *
from runner import *
from utils import *
import random

def main():
    # ================ Generar datos de prueba =========================
    test_sizes = [10, 100, 1000, 10000, 100000]
    
    
    # ================= Diccionario de funciones =======================
    funciones = {
        "benchmark": lambda: run_benchmark(test_sizes),
        "trinagulo": lambda: run_triangle_challenge(),
        
    }


    # ================= Ejecutar algoritmo elegido =====================
    algoritmo_ejecutar = "trinagulo"
    funciones[algoritmo_ejecutar]()

if __name__ == "__main__":
    main()
  
