# --- Importaciones de módulos ---
from .iterativos import (
    suma_digitos_iterativo,
    mcd_iterativo,
)

from .recursivos import (
    suma_digitos_recursivo,
    mcd_recursivo,
)

from .ordenamiento import (
    ordenamiento_mezcla,
    ordenamiento_mezcla_iterativo,
    ordenamiento_quicksort,
    ordenamiento_quicksort_iterativo,
)

# --- Lista de control para "from algoritmos import *" ---
__all__ = [
    # importaciones de iterativos
    "suma_digitos_iterativo",
    "mcd_iterativo",
    
    # importaciones de recursivos
    "suma_digitos_recursivo",
    "mcd_recursivo",
    
    # importaciones de ordenamiento
    "ordenamiento_mezcla",
    "ordenamiento_mezcla_iterativo",
    "ordenamiento_quicksort",
    "ordenamiento_quicksort_iterativo",
]
