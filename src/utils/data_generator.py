"""
Librería de generadores de estructuras de datos con elementos numéricos.
Proporciona funciones para crear arreglos, listas y pilas con contenido aleatorio.
"""

import random
from fractions import Fraction


def generar_arreglo(n, min_val=-100, max_val=100, incluir_racionales=False):
    """
    Genera un arreglo de tamaño n con números enteros o racionales aleatorios.
    
    Args:
        n (int): Tamaño del arreglo.
        min_val (int): Valor mínimo para números enteros (default: -100).
        max_val (int): Valor máximo para números enteros (default: 100).
        incluir_racionales (bool): Si True, incluye números racionales (default: False).
    
    Returns:
        list: Arreglo con n elementos aleatorios.
    
    Ejemplo:
        generar_arreglo(5) -> [-42, 15, -8, 99, 33]
        generar_arreglo(3, incluir_racionales=True) -> [1/2, 7, 3/4]
    """
    arreglo = []
    for _ in range(n):
        if incluir_racionales and random.choice([True, False]):
            numerador = random.randint(1, 10)
            denominador = random.randint(1, 10)
            arreglo.append(Fraction(numerador, denominador))
        else: arreglo.append(random.randint(min_val, max_val))
    return arreglo


def generar_lista(n, min_val=-100, max_val=100, incluir_racionales=False):
    """
    Genera una lista de tamaño n con números enteros o racionales aleatorios.
    
    Args:
        n (int): Tamaño de la lista.
        min_val (int): Valor mínimo para números enteros (default: -100).
        max_val (int): Valor máximo para números enteros (default: 100).
        incluir_racionales (bool): Si True, incluye números racionales (default: False).
    
    Returns:
        list: Lista con n elementos aleatorios.
    
    Ejemplo:
        generar_lista(4) -> [55, -12, 78, 3]
        generar_lista(3, incluir_racionales=True) -> [5/2, -8, 1/3]
    """
    return generar_arreglo(n, min_val, max_val, incluir_racionales)


def generar_pila(n, min_val=-100, max_val=100, incluir_racionales=False):
    """
    Genera una pila de tamaño n con números enteros o racionales aleatorios.
    
    Una pila se implementa como una lista donde el último elemento es la cima.
    
    Args:
        n (int): Tamaño de la pila.
        min_val (int): Valor mínimo para números enteros (default: -100).
        max_val (int): Valor máximo para números enteros (default: 100).
        incluir_racionales (bool): Si True, incluye números racionales (default: False).
    
    Returns:
        list: Pila con n elementos aleatorios (cima al final).
    
    Ejemplo:
        generar_pila(4) -> [10, -5, 42, 7]  # 7 es la cima
        generar_pila(3, incluir_racionales=True) -> [2/3, 9, 5/4]  # 5/4 es la cima
    """
    return generar_arreglo(n, min_val, max_val, incluir_racionales)


def generar_cola(n, min_val=-100, max_val=100, incluir_racionales=False):
    """
    Genera una cola de tamaño n con números enteros o racionales aleatorios.
    
    Una cola se implementa como una lista donde el primer elemento es el frente.
    
    Args:
        n (int): Tamaño de la cola.
        min_val (int): Valor mínimo para números enteros (default: -100).
        max_val (int): Valor máximo para números enteros (default: 100).
        incluir_racionales (bool): Si True, incluye números racionales (default: False).
    
    Returns:
        list: Cola con n elementos aleatorios (frente al inicio).
    
    Ejemplo:
        generar_cola(4) -> [15, -8, 63, 2]  # 15 es el frente
        generar_cola(3, incluir_racionales=True) -> [7/2, 5, 3/8]  # 7/2 es el frente
    """
    return generar_arreglo(n, min_val, max_val, incluir_racionales)


def generar_arreglo_ordenado(n, min_val=-100, max_val=100, orden="ascendente", incluir_racionales=False):
    """
    Genera un arreglo de tamaño n con números ordenados.
    
    Args:
        n (int): Tamaño del arreglo.
        min_val (int): Valor mínimo (default: -100).
        max_val (int): Valor máximo (default: 100).
        orden (str): "ascendente" o "descendente" (default: "ascendente").
        incluir_racionales (bool): Si True, incluye números racionales (default: False).
    
    Returns:
        list: Arreglo ordenado con n elementos.
    
    Ejemplo:
        generar_arreglo_ordenado(5) -> [-85, -42, 15, 61, 99]
        generar_arreglo_ordenado(5, orden="descendente") -> [98, 65, 32, -10, -67]
    """
    arreglo = generar_arreglo(n, min_val, max_val, incluir_racionales)
    if orden.lower() == "ascendente": arreglo.sort()
    elif orden.lower() == "descendente": arreglo.sort(reverse=True)
    return arreglo


def generar_arreglo_con_duplicados(n, min_val=-50, max_val=50, porcentaje_duplicados=0.3, incluir_racionales=False):
    """
    Genera un arreglo de tamaño n que puede contener elementos duplicados.
    
    Args:
        n (int): Tamaño del arreglo.
        min_val (int): Valor mínimo (default: -50).
        max_val (int): Valor máximo (default: 50).
        porcentaje_duplicados (float): Porcentaje de duplicados entre 0 y 1 (default: 0.3).
        incluir_racionales (bool): Si True, incluye números racionales (default: False).
    
    Returns:
        list: Arreglo con elementos y duplicados aleatorios.
    
    Ejemplo:
        generar_arreglo_con_duplicados(5) -> [12, 12, -5, 12, 8]
    """
    num_unicos = max(1, int(n * (1 - porcentaje_duplicados)))
    elementos = generar_arreglo(num_unicos, min_val, max_val, incluir_racionales)
    arreglo = elementos.copy()
    
    while len(arreglo) < n: arreglo.append(random.choice(elementos))
    
    random.shuffle(arreglo)
    return arreglo


def generar_arreglo_rango_restringido(n, rango_tuplas, incluir_racionales=False):
    """
    Genera un arreglo con elementos en rangos específicos alternados.
    
    Args:
        n (int): Tamaño del arreglo.
        rango_tuplas (list): Lista de tuplas (min, max) para cada rango.
        incluir_racionales (bool): Si True, incluye números racionales (default: False).
    
    Returns:
        list: Arreglo con elementos dentro de los rangos especificados.
    
    Ejemplo:
        generar_arreglo_rango_restringido(6, [(1, 10), (50, 100)])
        -> [7, 75, 3, 92, 9, 55]
    """
    arreglo = []
    for i in range(n):
        min_val, max_val = rango_tuplas[i % len(rango_tuplas)]
        if incluir_racionales and random.choice([True, False]):
            numerador = random.randint(min_val, max_val)
            denominador = random.randint(1, 10)
            arreglo.append(Fraction(numerador, denominador))
        else: arreglo.append(random.randint(min_val, max_val))
    
    random.shuffle(arreglo)
    return arreglo


def generar_arreglo_parcialmente_ordenado(n, min_val=-100, max_val=100, porcentaje_desordenado=0.5, incluir_racionales=False):
    """
    Genera un arreglo que está parcialmente ordenado.
    
    Args:
        n (int): Tamaño del arreglo.
        min_val (int): Valor mínimo (default: -100).
        max_val (int): Valor máximo (default: 100).
        porcentaje_desordenado (float): Porcentaje de elementos desordenados (default: 0.5).
        incluir_racionales (bool): Si True, incluye números racionales (default: False).
    
    Returns:
        list: Arreglo parcialmente ordenado.
    
    Ejemplo:
        generar_arreglo_parcialmente_ordenado(8, porcentaje_desordenado=0.5)
        -> [-85, -42, 88, 15, 61, 33, 99, 5]
    """
    arreglo = generar_arreglo_ordenado(n, min_val, max_val, incluir_racionales=incluir_racionales)
    num_desordenados = max(1, int(n * porcentaje_desordenado))
    
    for _ in range(num_desordenados):
        i = random.randint(0, n - 1)
        if incluir_racionales and random.choice([True, False]):
            numerador = random.randint(1, 10)
            denominador = random.randint(1, 10)
            arreglo[i] = Fraction(numerador, denominador)
        else: arreglo[i] = random.randint(min_val, max_val)
    
    return arreglo


def generar_matriz_ciudades(lengt):
    """
    Genera una matriz cuadrada de tamaño lengt x lengt.
    Los valores en la diagonal principal son 0.
    Los demás valores son números aleatorios entre 10 y 50.

    Parámetros:
        lengt (int): número de ciudades (tamaño de la matriz)

    Retorna:
        list[list[int]]: matriz generada
    """
    matriz = [
        [0 if i == j else random.randint(10, 50) for j in range(lengt)]
        for i in range(lengt)
    ]
    return matriz