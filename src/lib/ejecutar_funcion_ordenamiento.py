from colorama import Fore, Style
from algoritmos import *
from lib import *


# -------------------------------
# Funciones para ejecutar los algoritmos
# -------------------------------


def ejecutar_mergesort(arreglo: list):
    """
    Ejecuta el ordenamiento MergeSort y muestra los resultados en consola
    con colores para mayor claridad.

    Args:
        arreglo (list): La lista de elementos a ordenar.
    """
    print(Style.BRIGHT + f"\nOrdenamiento con MergeSort:")
    print(Fore.YELLOW + f"📜 Arreglo original: {arreglo}")
    
    arreglo_ordenado = ordenamiento_mergesort(arreglo.copy())
    
    print(Fore.GREEN + f"✨ Arreglo ordenado: {arreglo_ordenado}")
    print(Fore.MAGENTA + "──────────────────────────────────────────────────\n" + Style.RESET_ALL)


def ejecutar_quicksort(arreglo: list):
    """
    Ejecuta el ordenamiento QuickSort y muestra los resultados en consola
    con colores para mayor claridad.

    Args:
        arreglo (list): La lista de elementos a ordenar.
    """
    print(Style.BRIGHT + f"\nOrdenamiento con QuickSort:")
    print(Fore.YELLOW + f"📜 Arreglo original: {arreglo}")
    
    arreglo_ordenado = ordenamiento_quicksort(arreglo.copy())
    
    print(Fore.GREEN + f"✨ Arreglo ordenado: {arreglo_ordenado}")
    print(Fore.MAGENTA + "──────────────────────────────────────────────────\n" + Style.RESET_ALL)