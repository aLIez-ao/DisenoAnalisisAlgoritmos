"""
utils: generador de datos y algoritmos de ordenamiento.

Este paquete proporciona:
- Funciones para generar listas de prueba
- Implementaciones clásicas de algoritmos de ordenamiento
- Un sistema simple de configuración (DEBUG)
"""

# =================== Importar configuración interna ========================

# Importamos DEBUG y set_debug desde _config (fuente única de verdad)
from ._config import _DEBUG, set_debug

if _DEBUG:
    print("[utils] Inicializando paquete (modo debug activado)")


# =================== Importar funciones públicas ===========================

from .data_generator import (
    lista,
    lista_ordenada,
    lista_duplicados,
    lista_semiordenada,
    ciudad_matriz,
)

from .io_handlers import (
    read_campo_file,
    write_campo_file,
)

from .sorting import (
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

from .visualizer import plot_triangle_solution


# =================== API pública del paquete ===============================

__all__ = [
    # Utilidades de configuración 
    "_DEBUG",
    "set_debug",

    # Generación de datos
    "lista",
    "lista_ordenada",
    "lista_duplicados",
    "lista_semiordenada",
    "ciudad_matriz",
    
    # Handler
    'read_campo_file',
    'write_campo_file',

    # Algoritmos de ordenamiento
    "bubble_sort",
    "merge_sort",
    "selection_sort",
    "insertion_sort",
    "quick_sort",
    "heap_sort",
    "shell_sort",
    "counting_sort",
    "bogo_sort",
    
    # Visualizer
    'plot_triangle_solution',
]
