"""
Este módulo proporciona funciones para la lectura de archivos de texto (.txt) y la selección de archivos mediante una interfaz gráfica simple utilizando Tkinter.
Funciones:
- leer_txt(ruta: str) -> str: Lee el contenido de un archivo .txt y lo retorna como un string.
- seleccionar_txt() -> str: Abre un cuadro de diálogo para seleccionar un archivo .txt y retorna la ruta seleccionada.
Excepciones:
- FileNotFoundError: Si el archivo especificado no existe.
- UnicodeDecodeError: Si el archivo no puede ser decodificado como texto legible.
"""

import tkinter as tk
from tkinter import filedialog

def leer_txt(ruta: str) -> str:
    """
    Lee el contenido de un archivo .txt y lo retorna como un string.
    Args:
        ruta (str): Ruta del archivo .txt a leer.
    Returns:
        str: Contenido del archivo.
    Raises:
        FileNotFoundError: Si el archivo no existe.
        UnicodeDecodeError: Si el archivo no es texto legible.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        return contenido
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"No se pudo decodificar el archivo: {ruta}")


def seleccionar_txt() -> str:
    """
    Abre un explorador de archivos para seleccionar un archivo .txt.

    Returns:
        str: Ruta completa del archivo seleccionado, o cadena vacía si se cancela.
    """
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo .txt",
        filetypes=[("Archivos de texto", "*.txt")],
    )
    return ruta_archivo