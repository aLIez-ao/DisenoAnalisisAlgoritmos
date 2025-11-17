# src/lib/__init__.py

# --- Importaciones de funciones específicas ---
from .data_generator import (
    generar_arreglo,
    generar_lista,
    generar_pila,
    generar_cola,
    generar_arreglo_ordenado,
    generar_arreglo_con_duplicados,
    generar_arreglo_rango_restringido,
    generar_arreglo_parcialmente_ordenado,
    generar_matriz_ciudades,
)

from .sort import (
    bubble_sort,
    merge_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
    heap_sort,
    shell_sort,
    counting_sort,
    bogo_sort,
)

# --- Lista de control __all__ ---
__all__ = [
    # Funciones de generador_datos
    "generar_arreglo",
    "generar_lista",
    "generar_pila",
    "generar_cola",
    "generar_arreglo_ordenado",
    "generar_arreglo_con_duplicados",
    "generar_arreglo_rango_restringido",
    "generar_arreglo_parcialmente_ordenado",
    "generar_matriz_ciudades",
    
    # Funciones de sort
    "bubble_sort",
    "merge_sort",
    "selection_sort",
    "insertion_sort",
    "quick_sort",
    "heap_sort",
    "shell_sort",
    "counting_sort",
    "bogo_sort",
]