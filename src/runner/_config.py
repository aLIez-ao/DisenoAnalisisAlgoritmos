"""
_config.py — Configuración interna del paquete runner.

Este módulo gestiona el estado global y la inicialización de herramientas
transversales como Colorama. Se ejecuta automáticamente al importar el paquete.
"""

from colorama import init, Fore, Style


# ==================== CONFIGURACIÓN DE VARIABLES ================

init(autoreset=True)


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
    if _DEBUG:
        print(f"{Style.DIM}[DEBUG] Modo depuración ACTIVADO.{Style.RESET_ALL}")

def is_debug_active() -> bool:
    """Retorna el estado actual de la bandera DEBUG."""
    return _DEBUG

def log_debug(message: str) -> None:
    """
    Imprime un mensaje solo si el modo DEBUG está activo.
    Útil para trazar la ejecución sin ensuciar la salida normal.
    """
    if _DEBUG:
      print(f"{Style.DIM}[DEBUG] {message}{Style.RESET_ALL}")