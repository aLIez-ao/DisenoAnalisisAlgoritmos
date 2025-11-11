# src/algoritmos/__init__.py

from .optimizacion import (
    existe_par_suma_k,
    existe_par_suma_k_optimizado,
    busqueda_lineal,
    problema_mochila,
    problema_agente_viajero,
    producto_maximo,
    matriz_distancias,
)

from .recursivos import (
    suma_recursiva,
    contar_digitos,
    eliminar_medio,
    es_palindromo,
    fibonacci,
)

from .fuerza_Bruta import (
    cifrar_cesar,
    descifrar_cesar_fuerza_bruta,
    encontrar_maximo_producto,
)

from .ordenamiento import (
    ordenamiento_mergesort,
    ordenamiento_mergesort_iterativo,
    ordenamiento_quicksort,
    ordenamiento_quicksort_iterativo,
)

from .dinamicos import (
    resolver_laberinto,
)


# --- Lista de control __all__ ---
__all__ = [
    # De algoritmos_optimizacion
    'existe_par_suma_k',
    'existe_par_suma_k_optimizado',
    'busqueda_lineal',
    'problema_mochila',
    'problema_agente_viajero',
    'producto_maximo',
    "matriz_distancias",

    # De algoritmos_recursivos
    'suma_recursiva',
    'contar_digitos',
    'eliminar_medio',
    'es_palindromo',
    'fibonacci',

    # De algoritmos_fuerza_Bruta
    'cifrar_cesar',
    'descifrar_cesar_fuerza_bruta',
    'encontrar_maximo_producto',

    # De algoritmos_ordenamiento
    'ordenamiento_mergesort',
    'ordenamiento_mergesort_iterativo',
    'ordenamiento_quicksort',
    'ordenamiento_quicksort_iterativo',
    
    # De algoritmos_dinamicos
    'resolver_laberinto',
]