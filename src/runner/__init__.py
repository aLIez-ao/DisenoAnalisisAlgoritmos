# --- Importaciones de módulos ---
from .run_dominancia import (
    run_dominancia_nn,
    run_dominancia_nlogn,
)

from .run_iterativos import (
    run_suma_digitos_iterativo,
    run_mcd_iterativo,
)

from .run_recursivos import (
    run_suma_digitos_recursivo,
    run_mcd_recursivo,
)

from .run_ordenamiento import (
    run_mezcla,
    run_mezcla_iterativo,
    run_quicksort,
    run_quicksort_iterativo,
)

# --- Lista de control para "from algoritmos import *" ---
__all__ = [
    # importaciones de dominancia
    "run_dominancia_nn",
    "run_dominancia_nlogn",
    
    # importaciones de iterativos
    "run_suma_digitos_iterativo",
    "run_mcd_iterativo",
    
    # importaciones de recursivos
    "run_suma_digitos_recursivo",
    "run_mcd_recursivo",
    
    # importaciones de ordenamiento
    "run_mezcla",
    "run_mezcla_iterativo",
    "run_quicksort",
    "run_quicksort_iterativo",
    
]
