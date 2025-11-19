# src/runner/__init__.py

"""
Paquete runner.
Encargado de la ejecución, medición y visualización de benchmarks.
"""


# =================== Importar funciones públicas ===========================

from ._config import _DEBUG, _SPINNER_CHARS, set_debug, log_debug, is_debug_active
from .run_benchmarks import run_benchmark
from .run_challenge_triangle import run_triangle_challenge


if _DEBUG:
    print("[runner] Inicializando paquete (modo debug activado)")


# =================== API pública del paquete ===============================

__all__ = [
    # Utilidades de configuración 
    'set_debug',
    'log_debug',
    'is_debug_active',
    
    # Función
    'run_benchmark',
    'run_triangle_challenge',
]