# src/lib/__init__.py

# --- Importaciones de módulos ---
from .lector_txt import (
    leer_txt,
    leer_archivo,
)

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
    run_maximo_producto,
    run_cifrar_cesar,
    run_descifrar_cesar,
    run_cifrar_decifrar_cesar,
)


from .ejecutar_funcion_optimizacion import (
    run_par_suma_k,
    run_busqueda_lineal,
    run_problema_mochila,
    run_agente_viajero,
    run_producto_maximo_visual,
)


from .ejecutar_funcion_ordenamiento import (
    run_mergesort,
    run_quicksort,
)


from .ejecutar_funcion_recursiva import (
    run_suma_recursiva,
    run_contar_digitos,
    run_eliminar_medio,
    run_es_palindromo,
)


# --- Lista de control para "from lib import *" ---
# Esto le dice a main.py qué nombres importar.
__all__ = [
    # Módulos
    "leer_txt",
    "leer_archivo",

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
