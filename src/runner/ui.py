"""
src/runner/ui.py — Utilidades de Interfaz de Usuario.
"""
import sys
import time
import threading
import itertools
from colorama import Fore, Style
from ._config import SPINNER_CHARS

class Spinner:
    """
    Context Manager para mostrar una animación de carga en un hilo separado.
    Uso:
        with Spinner("Cargando datos"):
            funcion_lenta()
    """
    def __init__(self, message: str = "Procesando", delay: float = 0.1):
        self.message = message
        self.delay = delay
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._spin)

    def _spin(self):
        """Lógica de animación que corre en el hilo secundario."""
        spinner = itertools.cycle(SPINNER_CHARS)
        while not self.stop_event.is_set():
            sys.stdout.write(f"\r{Fore.YELLOW}{next(spinner)} {Fore.CYAN}{self.message}... {Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(self.delay)
        
        # Limpiar línea al terminar
        sys.stdout.write("\r" + " " * (len(self.message) + 10) + "\r")
        sys.stdout.flush()

    def __enter__(self):
        """Inicia el spinner al entrar al bloque 'with'."""
        self.stop_event.clear()
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Detiene el spinner al salir del bloque 'with'."""
        self.stop_event.set()
        self.thread.join()