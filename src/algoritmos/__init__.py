# src/algoritmos/__init__.py

from .algoritmos_optimizacion import (
    existe_par_suma_k,
    existe_par_suma_k_optimizado,
    busqueda_lineal,
    problema_mochila,
    problema_agente_viajero,
    producto_maximo,
    matriz_distancias,
)

from .algoritmos_recursivos import (
    suma_recursiva,
    contar_digitos,
    eliminar_medio,
    es_palindromo,
    fibonacci,
)

from .algoritmos_fuerza_Bruta import (
    cifrar_cesar,
    descifrar_cesar_fuerza_bruta,
    encontrar_maximo_producto,
)

from .algoritmos_ordenamiento import (
    ordenamiento_mergesort,
    ordenamiento_mergesort_iterativo,
    ordenamiento_quicksort,
    ordenamiento_quicksort_iterativo,
)

from .algoritmos_dinamicos import (
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