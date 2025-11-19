"""
_config.py — Configuración interna del paquete algoritmos.

Este módulo gestiona el estado global y la inicialización de herramientas.
Se ejecuta automáticamente al importar el paquete.
"""
#TODO: terminarl algoritmos/_config.py
# ==================== CONFIGURACIÓN DE VARIABLES ================



# ==================== BANDERAS DE ESTADO (Global) =======================

_DEBUG = False


# ==================== FUNCIONES DE ACCESO Y UTILIDAD ====================

def set_debug(value: bool) -> None:
    """
    Activa o desactiva el modo de depuración global.

    Args:
        value (bool): True para activar logs detallados.
    """
    global _DEBUG
    _DEBUG = value


def is_debug_active() -> bool:
    """Retorna el estado actual de la bandera DEBUG."""
    return _DEBUG


def log_debug(message: str) -> None:
    """
    Imprime un mensaje solo si el modo DEBUG está activo.
    Útil para trazar la ejecución sin ensuciar la salida normal.
    """
    if _DEBUG:
      print(f"[DEBUG] {message}")