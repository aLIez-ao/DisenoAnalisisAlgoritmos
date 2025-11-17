# usr/utils/sort.py
"""
Colección de algoritmos de ordenamiento en Python.

Este módulo proporciona implementaciones de varios algoritmos de ordenamiento
comunes de demostración.

Todas las funciones toman una lista de enteros y devuelven una nueva
lista ordenada, o modifican la lista in-situ y la devuelven.
"""

import random
from typing import List

# ============== BUBBLE SORT ==============
def bubble_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista usando el algoritmo Bubble Sort O(n²).

    Compara repetidamente pares de elementos adyacentes y los intercambia
    si están en el orden incorrecto. Incluye una optimización para
    detenerse si la lista ya está ordenada.

    Args:
        arr (List[int]): La lista de enteros a ordenar.

    Returns:
        List[int]: La lista ordenada.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# ============== MERGE SORT ==============
def merge_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista usando el algoritmo Merge Sort O(n log n).

    Utiliza la estrategia "divide y vencerás" para dividir la lista
    recursivamente y luego fusionar las sublistas ordenadas.

    Args:
        arr (List[int]): La lista de enteros a ordenar.

    Returns:
        List[int]: Una *nueva* lista ordenada (no modifica la original).
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Función auxiliar para merge_sort que fusiona dos listas ordenadas.

    Args:
        left (List[int]): La sublista izquierda ordenada.
        right (List[int]): La sublista derecha ordenada.

    Returns:
        List[int]: Una nueva lista fusionada y ordenada.
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ============== SELECTION SORT ==============
def selection_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista usando el algoritmo Selection Sort O(n²).

    En cada iteración, encuentra el elemento mínimo del resto de la
    lista y lo intercambia con el elemento en la posición actual.

    Args:
        arr (List[int]): La lista de enteros a ordenar.

    Returns:
        List[int]: La lista ordenada (modificada in-situ).
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# ============== INSERTION SORT ==============
def insertion_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista usando el algoritmo Insertion Sort O(n²).

    Construye la lista ordenada final un elemento a la vez, insertando
    cada nuevo elemento en su posición correcta dentro de la
    sublista ya ordenada.

    Args:
        arr (List[int]): La lista de enteros a ordenar.

    Returns:
        List[int]: La lista ordenada (modificada in-situ).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ============== QUICK SORT ==============
def quick_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista usando el algoritmo Quick Sort O(n log n).

    Utiliza "divide y vencerás" seleccionando un pivote y partiendo
    la lista en elementos menores, iguales y mayores que el pivote.
    Esta es una implementación recursiva simple.

    Args:
        arr (List[int]): La lista de enteros a ordenar.

    Returns:
        List[int]: Una *nueva* lista ordenada.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# ============== HEAP SORT ==============
def heap_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista usando el algoritmo Heap Sort O(n log n).

    Construye un Max Heap con la lista y luego extrae repetidamente
    el elemento máximo (raíz) y lo coloca al final de la lista.

    Args:
        arr (List[int]): La lista de enteros a ordenar.

    Returns:
        List[int]: La lista ordenada (modificada in-situ).
    """
    def heapify(arr, n, i):
        """
        Función auxiliar para mantener la propiedad de Max Heap.

        Args:
            arr (List[int]): El array (heap).
            n (int): Tamaño del heap.
            i (int): Índice del nodo raíz a "heapificar".
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    
    # Construir max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraer elementos del heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

# ============== SHELL SORT ==============
def shell_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista usando el algoritmo Shell Sort O(n log² n).

    Una generalización de Insertion Sort que permite el intercambio
    de elementos que están lejos, usando "gaps" decrecientes
    (secuencia de Knuth).

    Args:
        arr (List[int]): La lista de enteros a ordenar.

    Returns:
        List[int]: La lista ordenada (modificada in-situ).
    """
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr

# ============== COUNTING SORT ==============
def counting_sort(arr: List[int]) -> List[int]:
    """
    Ordena una lista usando el algoritmo Counting Sort O(n + k).

    Asume que la entrada es una colección de enteros en un rango
    definido. Cuenta la frecuencia de cada elemento para determinar
    sus posiciones finales. Es un algoritmo estable.

    Args:
        arr (List[int]): La lista de enteros a ordenar.

    Returns:
        List[int]: Una *nueva* lista ordenada.
    """
    if not arr:
        return arr
    
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    output = [0] * len(arr)
    
    # Contar ocurrencias
    for num in arr:
        count[num - min_val] += 1
    
    # Suma acumulada para obtener posiciones
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Construir la lista de salida
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output

# ============== BOGO SORT ==============
def bogo_sort(arr: List[int], max_iterations: int = 100000) -> List[int]:
    """
    Ordena una lista usando el (ineficiente) algoritmo Bogo Sort O(n!).

    Baraja la lista aleatoriamente hasta que esté ordenada.
    No recomendado para uso práctico; tiene una complejidad
    promedio de O((n+1)!).

    Args:
        arr (List[int]): La lista de enteros a ordenar.
        max_iterations (int, optional): Límite de intentos para
                                        evitar bucles casi infinitos.

    Returns:
        List[int]: La lista ordenada (si termina a tiempo).
    """
    def is_sorted(arr):
        """Comprueba si la lista está ordenada ascendentemente."""
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    iterations = 0
    while not is_sorted(arr) and iterations < max_iterations:
        random.shuffle(arr)
        iterations += 1
    
    if iterations >= max_iterations:
        print(f"⚠️ Bogo Sort no terminó en {max_iterations} iteraciones")
    
    return arr