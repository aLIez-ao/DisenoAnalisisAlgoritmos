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

# Bandera global para activar el modo debug en todo el paquete
DEBUG = False


def set_debug(value: bool) -> None:
    """
    Establece el valor de DEBUG globalmente.

    Parámetros
    ----------
    value : bool
        True para activar la impresión de mensajes de depuración.
        False para desactivarla.

    Notas
    -----
    - Esta función modifica una variable global *solo dentro de este módulo*.
    - Los módulos que importen la variable DEBUG deben leerla desde aquí
      usando:  `from ._config import DEBUG`.
    - Para modificar el valor global, es preferible llamar a esta función
      en lugar de modificar DEBUG manualmente.
    """
    global DEBUG
    DEBUG = value