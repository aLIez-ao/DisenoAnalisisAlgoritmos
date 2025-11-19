"""
Librería de generadores de estructuras de datos con elementos numéricos.
Proporciona funciones para crear listas con contenido aleatorio.
"""

import random
from fractions import Fraction
from ._config import DEBUG


# ====================  Helpers internos ==================================

def _debug(msg: str) -> None:
    """Imprime un mensaje solo si DEBUG está activado."""
    if DEBUG:
        print(f"[data_generator] {msg}")

def set_seed(seed=None) -> None:
    """Configura la semilla del generador aleatorio del módulo."""
    random.seed(seed)
    _debug(f"Semilla establecida a {seed}")

# ==================== Funciones Publicas ================================

def lista(n, min_v=-100, max_v=100, fracs=False, seed=None):
    """
    Genera una lista de tamaño n con números enteros o racionales aleatorios.

    Args:
        n (int): Tamaño de la lista.
        min_v (int): Valor mínimo para números enteros (default: -100).
        max_v (int): Valor máximo para números enteros (default: 100).
        fracs (bool): Si True, incluye números racionales (default: False).
        seed (int): Semilla para reproducibilidad (default: None).

    Returns:
        list: lista con n elementos aleatorios.
    """
    if seed is not None:
        set_seed(seed)

    array = []
    for _ in range(n):
        if fracs and random.choice([True, False]):
            num = random.randint(1, 10)
            den = random.randint(1, 10)
            array.append(Fraction(num, den))
        else:
            array.append(random.randint(min_v, max_v))

    return array


def lista_ordenada(n, min_v=-100, max_v=100, order="asc", fracs=False, seed=None):
    """
    Genera una lista de tamaño n con números ordenados.

    Args:
        n (int): Tamaño de la lista.
        min_v (int): Valor mínimo (default: -100).
        max_v (int): Valor máximo (default: 100).
        order (str): "asc" o "desc" (default: "asc").
        fracs (bool): Si True, incluye números racionales (default: False).
        seed (int): Semilla para reproducibilidad (default: None).

    Returns:
        list: lista ordenado con n elementos.
    """
    array = lista(n, min_v, max_v, fracs, seed)
    reverse = order.lower() in ["desc", "descendente"]
    array.sort(reverse=reverse)
    return array


def lista_duplicados(n, min_v=-50, max_v=50, dup_rate=0.3, fracs=False, seed=None):
    """
    Genera una lista de tamaño n que puede contener elementos duplicados.

    Args:
        n (int): Tamaño de la lista.
        min_v (int): Valor mínimo (default: -50).
        max_v (int): Valor máximo (default: 50).
        dup_rate (float): Tasa de duplicados entre 0 y 1 (default: 0.3).
        fracs (bool): Si True, incluye números racionales (default: False).
        seed (int): Semilla para reproducibilidad (default: None).

    Returns:
        list: lista con elementos y duplicados aleatorios.

    Ejemplo:
        lista_duplicados(5) -> [12, 12, -5, 12, 8]
    """
    if seed is not None:
        set_seed(seed)

    num_unique = max(1, int(n * (1 - dup_rate)))
    elements = lista(num_unique, min_v, max_v, fracs, seed=None)

    array = elements.copy()
    while len(array) < n:
        array.append(random.choice(elements))

    random.shuffle(array)
    return array


def lista_semiordenada(
    n, min_v=-100, max_v=100, unsorted_rate=0.5, fracs=False, seed=None
):
    """
    Genera una lista que está parcialmente ordenado.

    Args:
        n (int): Tamaño de la lista.
        min_v (int): Valor mínimo (default: -100).
        max_v (int): Valor máximo (default: 100).
        unsorted_rate (float): Tasa de elementos desordenados (default: 0.5).
        fracs (bool): Si True, incluye números racionales (default: False).
        seed (int): Semilla para reproducibilidad (default: None).

    Returns:
        list: lista parcialmente ordenado.

    Ejemplo:
        gen_partial_sorted(8, unsorted_rate=0.5) -> [-85, -42, 88, 15, 61, 33, 99, 5]
    """
    if seed is not None:
        set_seed(seed)

    array = lista(n, min_v, max_v, fracs=fracs, seed=None)
    num_unsorted = max(1, int(n * unsorted_rate))

    for _ in range(num_unsorted):
        i = random.randint(0, n - 1)

        if fracs and random.choice([True, False]):
            num = random.randint(1, 10)
            den = random.randint(1, 10)
            array[i] = Fraction(num, den)
        else:
            array[i] = random.randint(min_v, max_v)

    return array


def ciudad_matriz(size, seed=None):
    """
    Genera una matriz cuadrada de distancias entre ciudades.
    Los valores en la diagonal principal son 0.
    Los demás valores son números aleatorios entre 10 y 50.

    Args:
        size (int): Número de ciudades (tamaño de la matriz).
        seed (int): Semilla para reproducibilidad (default: None).

    Returns:
        list[list[int]]: Matriz de distancias generada.

    Ejemplo:
        cuidad_matriz(3) -> [[0, 25, 42], [18, 0, 31], [47, 15, 0]]
    """
    if seed is not None:
        set_seed(seed)

    matrix = [
        [0 if i == j else random.randint(10, 50) for j in range(size)]
        for i in range(size)
    ]

    return matrix

