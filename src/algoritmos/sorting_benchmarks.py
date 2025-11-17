#/usr/algorithmos/sorting_benchmarks.py
"""
Colección de algoritmos de ordenamiento en Python con un banco de pruebas
para medir su rendimiento y mostrar los resultados en una tabla.
"""

import random
import timeit
import sys
from utils import *
from typing import List, Callable, Dict, Any, Tuple

# Aumentamos el límite de recursión para Quick Sort en listas grandes
sys.setrecursionlimit(20000)



# ============== FUNCIÓN 1: MEDIR TIEMPOS ===========================

def measure_sorting_times(
    algorithms_to_test: List[Tuple[str, Callable]],
    sizes_to_test: List[int]
) -> Dict[str, Any]:
    """
    Mide el tiempo de ejecución de varios algoritmos de ordenamiento.

    Args:
        algorithms_to_test: Una lista de tuplas (nombre, funcion).
        sizes_to_test: Una lista de enteros con los tamaños de las listas a probar.

    Returns:
        Un diccionario con los resultados y metadatos para la tabla.
    """
    
    # Mapa de Big O para cada algoritmo
    big_o_map = {
        "Bubble Sort": "O(n^2)",
        "Selection Sort": "O(n^2)",
        "Insertion Sort": "O(n^2)",
        "Shell Sort": "O(n^2)",
        "Merge Sort": "O(n log n)",
        "Quick Sort": "O(n log n)",
        "Heap Sort": "O(n log n)",
        "Counting Sort": "O(n + k)",
        "Bogo Sort": "O((n+1)!)"
    }
    
    # Límites para algoritmos lentos
    N_SQUARED_CAP = 100000 # Límite para O(n^2)
    BOGO_CAP = 10         # Límite para Bogo Sort
    
    results: Dict[str, Dict[int, Any]] = {}

    print("Iniciando mediciones... (esto puede tardar varios segundos)")

    for name, func in algorithms_to_test:
        results[name] = {}
        print(f"  Probando: {name}...")

        for size in sizes_to_test:
            # --- Aplicar límites de seguridad ---
            if name == "Bogo Sort" and size > BOGO_CAP:
                results[name][size] = "N/A"
                continue
            
            if name in ["Bubble Sort", "Selection Sort", "Insertion Sort", "Shell Sort"] and size > N_SQUARED_CAP:
                results[name][size] = "N/A" # 'N/A' (No Aplicable)
                continue

            # --- Generar datos de prueba ---
            # Para Counting Sort, usamos un rango k más acotado (0-1000)
            if name == "Counting Sort":
                test_data = [random.randint(0, 1000) for _ in range(size)]
            else:
                # Rango de 0 al tamaño de la lista
                test_data = [random.randint(0, size) for _ in range(size)]
            
            # --- Medir el tiempo ---
            try:
                # Para listas pequeñas, promediamos 100 ejecuciones.
                # Para listas grandes, solo 1 ejecución es suficiente.
                number_of_runs = 100 if size <= 100 else 1
                
                # Usamos timeit para una medición precisa
                time_taken = timeit.timeit(
                    lambda: func(test_data.copy()), # ¡Importante pasar una copia!
                    number=number_of_runs
                ) / number_of_runs
                
                results[name][size] = time_taken
            
            except Exception as e:
                print(f"    ERROR en {name} con tamaño {size}: {e}")
                results[name][size] = "Error"

    print("Mediciones completadas.\n")
    
    return {
        "results": results,
        "algorithms": algorithms_to_test,
        "sizes": sizes_to_test,
        "big_o": big_o_map
    }
