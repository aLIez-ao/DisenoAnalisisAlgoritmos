from algoritmos import *
from runner import *
from utils import *
import random

def main():
    # ================ Generar datos de prueba =========================
    datos = {
       # Números individuales - generados dinámicamente
        "numero_pequeño": lambda: random.randint(1000, 99999),
        "numero_medio": lambda: random.randint(10**8, 10**12),
        "numero_grande": lambda: random.randint(10**30, 10**40),
        
        # Arreglos para ordenamiento - generados dinámicamente
        "arreglo_pequeño": lambda: lista(10, -50, 50),
        "arreglo_medio": lambda: lista(100, -100, 100),
        "arreglo_grande": lambda: lista(1000, -1000, 1000),
        "arreglo_muy_grande": lambda: lista(10000, -10000, 10000),
        
        # Listas, pilas y colas
        "lista_aleatoria": lambda: lista(random.randint(50, 150), -100, 100),
        "pila_aleatoria": lambda: lista(random.randint(20, 100), 0, 1000),
        "cola_aleatoria": lambda: lista(random.randint(30, 120), -500, 500),
        
    }
    
    test_sizes = [10, 100, 1000, 10000, 100000]
    
    
    # ================= Diccionario de funciones =======================

    funciones = {
        # Benchmark
        # TODO: arreglar el metodo
        "benchmark": lambda: run_benchmark(test_sizes),
        
        
    }


    # ================= Ejecutar algoritmo elegido =====================

    algoritmo_ejecutar = "benchmark"
    funciones[algoritmo_ejecutar]()

if __name__ == "__main__":
    main()
  
