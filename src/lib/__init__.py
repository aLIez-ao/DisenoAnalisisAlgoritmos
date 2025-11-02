# --- Importaciones de módulos ---
from .ejecutar_iterativos import (
    ejecutar_suma_digitos_iterativo,
    ejecutar_mcd_iterativo,
)

from .ejecutar_recursivos import (
    ejecutar_suma_digitos_recursivo,
    ejecutar_mcd_recursivo,
)

from .ejecutar_ordenamiento import (
    ejecutar_mezcla,
    ejecutar_mezcla_iterativo,
    ejecutar_quicksort,
    ejecutar_quicksort_iterativo,
)

from .generador_datos import (
    generar_arreglo,
    generar_lista,
    generar_pila,
    generar_cola,
    generar_arreglo_ordenado,
    generar_arreglo_con_duplicados,
    generar_arreglo_rango_restringido,
    generar_arreglo_parcialmente_ordenado,
)

# --- Lista de control para "from algoritmos import *" ---
__all__ = [
    # importaciones de iterativos
    "ejecutar_suma_digitos_iterativo",
    "ejecutar_mcd_iterativo",
    
    # importaciones de recursivos
    "ejecutar_suma_digitos_recursivo",
    "ejecutar_mcd_recursivo",
    
    # importaciones de ordenamiento
    "ejecutar_mezcla",
    "ejecutar_mezcla_iterativo",
    "ejecutar_quicksort",
    "ejecutar_quicksort_iterativo",
    
    # importaciones de generador_datos
    "generar_arreglo",
    "generar_lista",
    "generar_pila",
    "generar_cola",
    "generar_arreglo_ordenado",
    "generar_arreglo_con_duplicados",
    "generar_arreglo_rango_restringido",
    "generar_arreglo_parcialmente_ordenado",
]
