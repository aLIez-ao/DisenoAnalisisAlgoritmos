# src/lib/__init__.py

# --- Importaciones de módulos ---
from .laberinto import (
    leer_dimensiones,
    procesar_linea,
    buscar_entradas_y_salidas,
    cargar_laberinto,
    
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
    generar_matriz_ciudades,
)

from .lector_txt import (
    leer_txt,
    leer_archivo,
)

# # --- Lista de control __all__ ---
__all__ = [
    # Funciones de laberinto
    "leer_dimensiones",
    "procesar_linea",
    "buscar_entradas_y_salidas",
    "cargar_laberinto",

    # Funciones de generador_datos
    "generar_arreglo",
    "generar_lista",
    "generar_pila",
    "generar_cola",
    "generar_arreglo_ordenado",
    "generar_arreglo_con_duplicados",
    "generar_arreglo_rango_restringido",
    "generar_arreglo_parcialmente_ordenado",
    "generar_matriz_ciudades",
    
    # Lectores de archivos
    "leer_txt",
    "leer_archivo",
]
