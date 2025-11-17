# --- Importaciones de módulos ---
from .dominancia import (
    dominancia_nn,
    dominancia_nlogn
)

from .iterativos import (
    suma_digitos_iterativo,
    mcd_iterativo,
)

from .recursivos import (
    suma_digitos_recursivo,
    mcd_recursivo,
)

from .ordenamiento import (
    mergesort,
    mergesort_iterativo,
    quicksort,
    quicksort_iterativo,
)

# --- Lista de control para "from algoritmos import *" ---
__all__ = [
    # importaciones de dominancia
    "dominancia_nn",
    "dominancia_nlogn",
    
    # importaciones de iterativos
    "suma_digitos_iterativo",
    "mcd_iterativo",
    
    # importaciones de recursivos
    "suma_digitos_recursivo",
    "mcd_recursivo",
    
    # importaciones de ordenamiento
    "mergesort",
    "mergesort_iterativo",
    "quicksort",
    "quicksort_iterativo",
]
