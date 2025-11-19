"""

"""
# TODO: Documentar el paquete

# ================== Activar/Desactivar modo debug ==========================

DEBUG = False

if DEBUG:
    print("[algoritmos] Inicializando paquete (modo debug activado)")



# ================== Evitar errores si los módulos fallan ==================
# TODO: Completar los modulos
try:
    from .benchmarks import (
        measure_sorting_performance,
        
    )
except Exception as e:
    raise ImportError(f"[algortimos] Error al cargar benchmarks.py: {e}")


# ================== Inicialización global: Semilla ====================

# TODO: revisar si es necesario



# ================== Generación automática de __all__ ==================

__all__ = [
    # Funciones de benchmarks
    "measure_sorting_performance",
]
