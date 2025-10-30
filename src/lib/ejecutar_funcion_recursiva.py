import random
from typing import List, Tuple
from colorama import Fore, Style
from algoritmos import *
from lib import *
from .lector_txt import leer_txt


# -------------------------------
# Funciones para ejecutar los algoritmos
# -------------------------------


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
