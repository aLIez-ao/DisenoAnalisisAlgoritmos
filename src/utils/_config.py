"""
_config.py — Configuración interna del paquete utils.

Este módulo contiene variables y funciones de configuración que afectan
al comportamiento global del paquete. El prefijo '_' indica que es un
módulo interno y no forma parte de la API pública oficial, aunque las
configuraciones pueden exponerse desde utils/__init__.py.

Contenido:
- DEBUG: bandera global para activar/desactivar mensajes de depuración.
- set_debug(): función segura para modificar la bandera DEBUG.
"""

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