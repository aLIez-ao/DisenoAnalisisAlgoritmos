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

# # --- Lista de control __all__ ---
__all__ = [
    # Lectores de archivos
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
]
