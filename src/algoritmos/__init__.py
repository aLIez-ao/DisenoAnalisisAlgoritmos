""" """

# TODO: Documentar el paquete

# =================== Importar funciones públicas ===========================

# TODO: Completar los modulos
from ._config import _DEBUG, set_debug, log_debug, is_debug_active
from .benchmarks import measure_sorting_performance


if _DEBUG:
    print("[algoritmos] Inicializando paquete (modo debug activado)")


# =================== API pública del paquete ===============================

__all__ = [
    # Utilidades de configuración
    "set_debug",
    "log_debug",
    "is_debug_active",
    
    # Funciones de benchmarks
    "measure_sorting_performance",
]
