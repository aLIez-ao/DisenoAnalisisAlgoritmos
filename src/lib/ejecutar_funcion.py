"""
Este módulo contiene funciones utilitarias para ejecutar y mostrar resultados de diversos algoritmos clásicos,
principalmente para propósitos educativos y de demostración en consola. Proporciona funciones que llaman a
implementaciones de algoritmos importados y presentan sus resultados de forma formateada y colorida usando colorama.
Requiere:
- colorama para la salida colorida en consola.
- algoritmos.py con las implementaciones de los algoritmos llamados.
Uso:
Importar este módulo y llamar a las funciones de ejecución pasando los argumentos requeridos.
"""

import random
from typing import List, Tuple
from colorama import Fore, Style
from algoritmos import *
from lib import *
from .lector_txt import leer_txt


# -------------------------------
# Funciones para ejecutar los algoritmos
# -------------------------------


def ejecutar_par_suma_k(arreglo):
    """
    Busca y ejecuta algoritmos para encontrar un par de números en el arreglo
    que sumen un valor k (calculado aleatoriamente a partir de dos elementos).

    Compara dos versiones: la búsqueda estándar y la optimizada.

    Args:
        arreglo (list): Lista de enteros donde se buscarán los pares.

    Returns:
        None. Imprime en consola los resultados de ambas búsquedas.

    Nota:
        - Selecciona aleatoriamente dos índices del arreglo
        - Calcula k como la suma de los elementos en esos índices
        - Ejecuta dos funciones de búsqueda para comparar resultados
    """
    i, j = random.sample(range(len(arreglo)), 2)
    k = arreglo[i] + arreglo[j]
    print(Style.BRIGHT + f"\n{'='*40}")
    print(Style.BRIGHT + f" Buscando si existe un par que sume {k} ")
    print(f"{'='*40}\n")
    existe_par_suma_k(arreglo, k)
    existe_par_suma_k_optimizado(arreglo, k)


def ejecutar_busqueda_lineal(arreglo, valor):
    """
    Ejecuta la búsqueda lineal de un valor en el arreglo e imprime
    el resultado con información sobre comparaciones realizadas.

    Args:
        arreglo (list): Lista de enteros donde se realizará la búsqueda.
        valor (int): El valor a buscar en el arreglo.

    Returns:
        None. Imprime en consola el índice encontrado o mensaje de no encontrado,
        junto con el número de comparaciones realizadas.

    Output:
        - Mensaje de éxito en verde si se encuentra el valor
        - Mensaje de error en rojo si no se encuentra
        - Número total de comparaciones realizadas
    """
    indice, comparaciones = busqueda_lineal(arreglo, valor)
    print(Style.BRIGHT + f"\nBúsqueda lineal del valor {valor}:")
    if indice != -1: print(Fore.GREEN + f"✅ Valor encontrado en índice {indice}")
    else: print(Fore.RED + "❌ Valor no encontrado.")
    print(f"Número de comparaciones realizadas: {comparaciones}\n")


def ejecutar_suma_recursiva(lista):
    """
    Calcula la suma de todos los elementos en una lista utilizando recursión
    e imprime el resultado de forma formateada.

    Args:
        lista (list): Lista de números (int o float) a sumar recursivamente.

    Returns:
        None. Imprime en consola la lista y el resultado de la suma.

    Output:
        - Lista original
        - Resultado de la suma en color verde

    Ejemplo:
        ejecutar_suma_recursiva([1, 2, 3, 4, 5])
        # Output: Suma recursiva de la lista [1, 2, 3, 4, 5]:
        #         Resultado: 15
    """
    print(Style.BRIGHT + f"\nSuma recursiva de la lista {lista}:")
    print(Fore.GREEN + f"Resultado: {suma_recursiva(lista)}\n")


def ejecutar_contar_digitos(n):
    """
    Cuenta el número de dígitos en un número entero utilizando recursión
    e imprime el resultado.

    Args:
        n (int): Número entero del cual contar los dígitos.

    Returns:
        None. Imprime en consola el número y la cantidad de dígitos.

    Output:
        - Número analizado
        - Cantidad de dígitos en color verde

    Ejemplo:
        ejecutar_contar_digitos(12345)
        # Output: Contar dígitos del número 12345:
        #         Resultado: 5
    """
    digitos = contar_digitos(n)
    print(Style.BRIGHT + f"\nContar dígitos del número {n}:")
    print(Fore.GREEN + f"Resultado: {digitos}\n")


def ejecutar_eliminar_medio(pila):
    """
    Elimina el elemento del medio de una pila e imprime el resultado
    antes y después de la operación.

    Args:
        pila (list): Pila (lista) de la cual eliminar el elemento medio.

    Returns:
        None. Modifica la pila in-place y imprime el resultado.

    Output:
        - Pila original (copia para mostrar)
        - Pila después de eliminar el elemento del medio en color verde

    Nota:
        - Si la pila tiene longitud par, se elimina el elemento superior del medio
        - La función modifica la lista original

    Ejemplo:
        ejecutar_eliminar_medio([1, 2, 3, 4, 5])
        # Output: Pila original: [1, 2, 3, 4, 5]
        #         Pila después de eliminar el medio: [1, 2, 4, 5]
    """
    pila_copia = pila.copy()
    print(Style.BRIGHT + f"\nEliminar el elemento medio de la pila {pila_copia}:")
    eliminar_medio(pila_copia)
    print(Fore.GREEN + f"Pila después de eliminar el medio: {pila_copia}\n")


def ejecutar_es_palindromo(cadena):
    """
    Verifica si una cadena de texto es un palíndromo e imprime el resultado
    de forma visual con indicadores de éxito o fracaso.

    Args:
        cadena (str): Cadena de caracteres a verificar.

    Returns:
        None. Imprime en consola si la cadena es o no un palíndromo.

    Output:
        - Mensaje en verde (✅) si es palíndromo
        - Mensaje en rojo (❌) si no es palíndromo

    Ejemplo:
        ejecutar_es_palindromo("anilina")
        # Output: Verificar si la cadena 'anilina' es un palíndromo:
        #         ✅ Es un palíndromo.

        ejecutar_es_palindromo("hola")
        # Output: Verificar si la cadena 'hola' es un palíndromo:
        #         ❌ No es un palíndromo.
    """
    print(Style.BRIGHT + f"\nVerificar si la cadena '{cadena}' es un palíndromo:")
    if es_palindromo(cadena): print(Fore.GREEN + "✅ Es un palíndromo.\n")
    else: print(Fore.RED + "❌ No es un palíndromo.\n")


def ejecutar_maximo_producto(arreglo):
    """
    Prueba la función encontrar_maximo_producto con estilo colorido en consola.

    Args:
        arreglo: Lista de enteros a procesar
    """
    num1, num2, producto_maximo = encontrar_maximo_producto(arreglo)

    print(Style.BRIGHT + f"\n{'='*60}")
    print(f"Búsqueda del máximo producto de dos números:")
    print(f"{'='*60}")
    print(f"Arreglo: {arreglo}")

    print(Style.BRIGHT + Fore.CYAN + f"\n📊 Resultado:")
    print(Fore.GREEN + f"✅ Los dos números con producto máximo: {num1} × {num2}")
    print(Fore.YELLOW + f"🎯 Producto máximo: {producto_maximo}\n")
    print(f"{'='*60}\n")


def ejecutar_cifrar_cesar(texto: str, desplazamiento: int, alfabeto: str):
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


def ejecutar_descifrar_cesar(texto_encriptado: str, alfabeto: str):
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


def ejecutar_cifrar_decifrar_cesar(ruta: str, desplazamiento: int, alfabeto: str):
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
    ejecutar_descifrar_cesar(texto_encriptado, alfabeto)