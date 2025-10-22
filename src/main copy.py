import time
from algoritmos import *
from lib import generar_arreglo

if __name__ == "__main__":

    arreglo = generar_arreglo(20)
    print("Arreglo original: ", arreglo)

    # Merge Sort recursivo
    inicio = time.time()
    arreglo_ordenado_1 = ordenamiento_mezcla(arreglo)
    fin = time.time()
    print("Merge Sort recursivo: ", arreglo_ordenado_1)
    print(f"Tiempo: {fin - inicio:.6f} segundos\n")

    # Merge Sort iterativo
    inicio = time.time()
    arreglo_ordenado_2 = ordenamiento_mezcla_iterativo(arreglo.copy())
    fin = time.time()
    print("Merge Sort iterativo: ", arreglo_ordenado_2)
    print(f"Tiempo: {fin - inicio:.6f} segundos\n")

    # Quicksort iterativo
    inicio = time.time()
    arreglo_ordenado_4 = ordenamiento_quicksort_iterativo(arreglo.copy())
    fin = time.time()
    print("Quicksort iterativo: ", arreglo_ordenado_4)
    print(f"Tiempo: {fin - inicio:.6f} segundos\n")
    
    # Quicksort recursivo
    inicio = time.time()
    arreglo_ordenado_3 = ordenamiento_quicksort(arreglo)
    fin = time.time()
    print("Quicksort recursivo: ", arreglo_ordenado_3)
    print(f"Tiempo: {fin - inicio:.6f} segundos\n")
