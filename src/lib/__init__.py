# src/lib/__init__.py

# --- Importaciones de módulos ---
from . import lector_txt

# --- Importaciones de funciones específicas ---
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

from .ejecutar_funcion_fuerza_bruta import (
    ejecutar_maximo_producto,
    ejecutar_cifrar_cesar,
    ejecutar_descifrar_cesar,
    ejecutar_cifrar_decifrar_cesar,
)


from .ejecutar_funcion_optimizacion import (
    ejecutar_par_suma_k,
    ejecutar_busqueda_lineal,
    ejecutar_problema_mochila,
    ejecutar_agente_viajero,
    ejecutar_producto_maximo_visual,
)


from .ejecutar_funcion_ordenamiento import (
    ejecutar_mergesort,
    ejecutar_quicksort,
)


from .ejecutar_funcion_recursiva import (
    ejecutar_suma_recursiva,
    ejecutar_contar_digitos,
    ejecutar_eliminar_medio,
    ejecutar_es_palindromo,
)


# --- Lista de control para "from lib import *" ---
# Esto le dice a main.py qué nombres importar.
__all__ = [
    # Módulos
    "lector_txt",

    # Funciones de generador_datos
    "generar_arreglo",
    "generar_lista",
    "generar_pila",
    "generar_cola",
    "generar_arreglo_ordenado",
    "generar_arreglo_con_duplicados",
    "generar_arreglo_rango_restringido",
    "generar_arreglo_parcialmente_ordenado",

    # Funciones de ordenamiento
    "ejecutar_mergesort",
    "ejecutar_quicksort",

    # Funciones de optimización
    "ejecutar_par_suma_k",
    "ejecutar_busqueda_lineal",
    "ejecutar_problema_mochila",
    "ejecutar_problema_mochila",
    'ejecutar_agente_viajero',
    'ejecutar_producto_maximo_visual',

    # Funciones recursivas
    "ejecutar_suma_recursiva",
    "ejecutar_contar_digitos",
    "ejecutar_eliminar_medio",
    "ejecutar_es_palindromo",

    # Funciones de fuerza bruta / cifrado
    "ejecutar_maximo_producto",
    "ejecutar_cifrar_cesar",
    "ejecutar_descifrar_cesar",
    "ejecutar_cifrar_decifrar_cesar",
]
