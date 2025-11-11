from colorama import Fore, Style
from algoritmos import *
from utils import *

# -------------------------------
# Funciones para ejecutar los algoritmos
# -------------------------------


def run_maximo_producto(arreglo):
    """
    Prueba la función encontrar_maximo_producto con estilo colorido en consola.
    """
    resultado = encontrar_maximo_producto(arreglo)
    if resultado is None or None in resultado:
        print(Fore.RED + "⚠️ No se pudo calcular el producto máximo (arreglo insuficiente o vacío).")
        return

    num1, num2, producto_maximo = resultado

    print(Style.BRIGHT + f"\n{'='*60}")
    print(f"Búsqueda del máximo producto de dos números:")
    print(f"{'='*60}")
    print(f"Arreglo: {arreglo}")

    print(Style.BRIGHT + Fore.CYAN + f"\n📊 Resultado:")
    print(Fore.GREEN + f"✅ Los dos números con producto máximo: {num1} × {num2}")
    print(Fore.YELLOW + f"🎯 Producto máximo: {producto_maximo}\n")
    print(f"{'='*60}\n")


def run_cifrar_cesar(texto: str, desplazamiento: int, alfabeto: str):
    """
    Ejecuta el cifrado César y muestra el resultado en consola con estilo visual.

    Args:
        texto (str): Texto a cifrar.
        alfabeto (str): Cadena de caracteres permitidos en el cifrado.
        desplazamiento (int): Número de posiciones para el cifrado.

    Returns:
        None. Imprime en consola el resultado del cifrado.

    Output:
        - Mensaje en amarillo mostrando el texto original
        - Mensaje en cian mostrando el desplazamiento
        - Mensaje en verde mostrando el texto cifrado
    """
    print(Style.BRIGHT + f"\nCifrado César del texto:")
    print(Fore.YELLOW + f"📜 Texto original: '{texto}'")
    print(Fore.CYAN + f"🔢 Desplazamiento: {desplazamiento}")

    texto_cifrado = cifrar_cesar(texto, alfabeto, desplazamiento)

    print(Fore.GREEN + f"🔐 Texto cifrado: '{texto_cifrado}'\n" + Style.RESET_ALL)


def run_descifrar_cesar(texto_encriptado: str, alfabeto: str):
    """
    Ejecuta el descifrado César por fuerza bruta e imprime los resultados
    con colores, destacando los candidatos más legibles.
    """
    print(Style.BRIGHT + f"\nDescifrado por fuerza bruta del texto:")
    print(Fore.YELLOW + f"🔐 Texto cifrado: '{texto_encriptado}'")
    print(Style.RESET_ALL)

    resultados = descifrar_cesar_fuerza_bruta(texto_encriptado, alfabeto)
    print(Fore.CYAN + "Posibles descifrados:\n" + Style.RESET_ALL)

    for desplazamiento, texto in resultados:
        print(f"{Fore.WHITE}Desplazamiento {desplazamiento:2d}:{Fore.RESET} {texto}")

    print(Fore.MAGENTA + "\n──────────────────────────────────────────────\n" + Style.RESET_ALL)


def run_cifrar_decifrar_cesar(ruta: str, desplazamiento: int, alfabeto: str):
    """
    Ejecuta el cifrado César sobre el contenido de un archivo .txt y luego
    realiza un descifrado por fuerza bruta mostrando todos los posibles
    desplazamientos.
    La función imprime en consola:
        - El texto original leído del archivo.
        - El desplazamiento utilizado para el cifrado.
        - El texto cifrado.
        - Todos los posibles descifrados por fuerza bruta, resaltando
          los que podrían ser legibles.
    Args:
        ruta (str): Ruta del archivo .txt a leer.
        desplazamiento (int): Número de posiciones que se desplazará cada carácter.
        alfabeto (str): Cadena que representa el alfabeto permitido. 
                        Ejemplo: "abcdefghijklmnñopqrstuvwxyz ,."
    Raises:
        FileNotFoundError: Si el archivo no existe en la ruta especificada.
        UnicodeDecodeError: Si el archivo no se puede decodificar como texto.
    Salida en consola:
        - Texto original
        - Texto cifrado
        - Tabla de posibles descifrados por fuerza bruta
    """
    texto = leer_txt(ruta)
    
    print(Style.BRIGHT + f"\nCifrado César del texto:")
    print(Fore.YELLOW + f"📜 Texto original: '{texto}'")
    print(Fore.CYAN + f"🔢 Desplazamiento: {desplazamiento}")

    texto_encriptado = cifrar_cesar(texto, alfabeto, desplazamiento)

    print(Fore.GREEN + f"🔐 Texto cifrado: '{texto_encriptado}'\n" + Style.RESET_ALL)
    run_descifrar_cesar(texto_encriptado, alfabeto)