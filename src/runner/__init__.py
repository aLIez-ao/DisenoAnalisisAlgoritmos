# src/lib/__init__.py

# --- Importaciones de módulos ---
from .run_fuerza_bruta import (
    run_maximo_producto,
    run_cifrar_cesar,
    run_descifrar_cesar,
    run_cifrar_decifrar_cesar,
)


from .run_optimizacion import (
    run_par_suma_k,
    run_busqueda_lineal,
    run_problema_mochila,
    run_agente_viajero,
    run_producto_maximo_visual,
)


from .run_ordenamiento import (
    run_mergesort,
    run_quicksort,
)


from .run_recursiva import (
    run_suma_recursiva,
    run_contar_digitos,
    run_eliminar_medio,
    run_es_palindromo,
)


# --- Lista de control __all__ ---
__all__ = [
   # Funciones de ordenamiento
    "run_mergesort",
    "run_quicksort",

    # Funciones de optimización
    "run_par_suma_k",
    "run_busqueda_lineal",
    "run_problema_mochila",
    "run_problema_mochila",
    'run_agente_viajero',
    'run_producto_maximo_visual',

    # Funciones recursivas
    "run_suma_recursiva",
    "run_contar_digitos",
    "run_eliminar_medio",
    "run_es_palindromo",

    # Funciones de fuerza bruta / cifrado
    "run_maximo_producto",
    "run_cifrar_cesar",
    "run_descifrar_cesar",
    "run_cifrar_decifrar_cesar",
]
