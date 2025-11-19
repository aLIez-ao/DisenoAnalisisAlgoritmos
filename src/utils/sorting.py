"""
Módulo de algoritmos de ordenamiento.

Proporciona implementaciones didácticas de algoritmos clásicos de sorting.
Todas las funciones devuelven una nueva lista ordenada y **no modifican**
la lista original (a menos que se indique explícitamente con `inplace=True`).

Compatibles con cualquier tipo de dato comparable: int, float, Fraction, etc.
"""

from typing import Protocol, Self, TypeVar, List
import random

class Comparable(Protocol):
    def __lt__(self: Self, other: Self) -> bool: ...
    def __gt__(self: Self, other: Self) -> bool: ...
    def __le__(self: Self, other: Self) -> bool: ...
    def __ge__(self: Self, other: Self) -> bool: ...
    def __eq__(self: Self, other: Self) -> bool: ...

T = TypeVar("T", bound=Comparable)


# ======================= Utilidad interna ==============================

def _maybe_copy(arr: List[T], inplace: bool) -> List[T]:
    """Devuelve una copia de la lista si inplace=False."""
    return arr if inplace else arr.copy()


# ======================= BUBBLE SORT ====================================

def bubble_sort(arr: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]:
    """
    Ordena una lista usando Bubble Sort O(n²).

    Args:
        arr: Lista de elementos comparables.
        reverse: Si True, ordena de mayor a menor.
        inplace: Si True, modifica la lista original.

    Returns:
        Una lista ordenada.
    """
    arr = _maybe_copy(arr, inplace)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


# ======================= SELECTION SORT ====================================

def selection_sort(arr: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]:
    """
    Ordena una lista usando Selection Sort O(n²).

    Args:
        arr: Lista de elementos comparables.
        reverse: Si True, orden descendente.
        inplace: Si True, modifica la lista original.

    Returns:
        Lista ordenada.
    """
    arr = _maybe_copy(arr, inplace)
    n = len(arr)

    for i in range(n):
        selected = i
        for j in range(i + 1, n):
            if (arr[j] < arr[selected]) ^ reverse:
                selected = j
        arr[i], arr[selected] = arr[selected], arr[i]

    return arr


# ======================= INSERTION SORT ====================================

def insertion_sort(arr: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]:
    """
    Ordena una lista usando Insertion Sort O(n²).

    Args:
        arr: Lista de elementos comparables.
        reverse: Si True, orden descendente.
        inplace: Si True, modifica la lista original.

    Returns:
        Lista ordenada.
    """
    arr = _maybe_copy(arr, inplace)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and (arr[j] > key) ^ reverse:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# ======================= SHELL SORT ====================================

def shell_sort(arr: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]:
    """
    Ordena una lista usando Shell Sort con la secuencia de Knuth.

    Complejidad típica: O(n^(3/2))
    Peor caso: O(n^2)
    Mejor caso: O(n log n)

    Args:
        arr: Lista de elementos comparables.
        reverse: Si True, orden descendente.
        inplace: Si True, modifica la lista original.

    Returns:
        Lista ordenada.
    """
    arr = _maybe_copy(arr, inplace)
    n = len(arr)

    # Secuencia de Knuth
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1

    # Shell sort
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Comparación ajustada con XOR para reverse
            while j >= gap and ((arr[j - gap] > temp) ^ reverse):
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 3

    return arr


# ======================= MERGE SORT ====================================

def merge_sort(arr: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]:
    """
    Ordena una lista usando merge (O(n log n)).

    Args:
        arr: Lista de elementos comparables.
        reverse: Si True, ordena de mayor a menor.
        inplace: Si True, modifica la lista original.

    Returns:
        Una lista ordenada.
    """
    arr = _maybe_copy(arr, inplace)
    _merge_sort_recursive(arr, 0, len(arr) - 1, reverse)
    return arr

def _merge_sort_recursive(arr: List[T], left: int, right: int, reverse: bool):
    if left < right:
        mid = (left + right) // 2

        _merge_sort_recursive(arr, left, mid, reverse)
        _merge_sort_recursive(arr, mid + 1, right, reverse)
        
        _merge_inplace_simulation(arr, left, mid, right, reverse)

def _merge_inplace_simulation(arr: List[T], left: int, mid: int, right: int, reverse: bool):
    """Mezcla dos sub-arrays usando una lista temporal solo para esa sección."""
    n1 = mid - left + 1
    n2 = right - mid

    # Creamos copias temporales SOLO de la sección necesaria
    L = arr[left : mid + 1]
    R = arr[mid + 1 : right + 1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if (L[i] <= R[j]) ^ reverse:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar remanentes
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# ======================= QUICK SORT ====================================

def quick_sort(arr: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]:
    """
    Ordena una lista usando quick sort (O(n log n)).

    Args:
        arr: Lista de elementos comparables.
        reverse: Si True, ordena de mayor a menor.
        inplace: Si True, modifica la lista original.

    Returns:
        Una lista ordenada.
    """
    # 1. Gestión de la copia (API Pública)
    arr = _maybe_copy(arr, inplace)

    # 2. Llamada a la función recursiva interna
    _quick_sort_recursive(arr, 0, len(arr) - 1, reverse)
    
    return arr

def _quick_sort_recursive(arr: List[T], low: int, high: int, reverse: bool):
    """Función interna recursiva que trabaja con índices."""
    if low < high:
        # Obtener el índice del pivote ya ordenado
        pi = _partition(arr, low, high, reverse)

        # Ordenar los elementos antes y después de la partición
        _quick_sort_recursive(arr, low, pi - 1, reverse)
        _quick_sort_recursive(arr, pi + 1, high, reverse)

def _partition(arr: List[T], low: int, high: int, reverse: bool) -> int:
    """Coloca el pivote en su lugar correcto."""
    pivot = arr[high]
    i = low - 1  # Índice del elemento más pequeño

    for j in range(low, high):
        # La magia del XOR para invertir la lógica
        if (arr[j] < pivot) ^ reverse: 
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ======================= HEAP SORT ====================================

def heap_sort(arr: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]:
    """
    Ordena una lista usando Heap Sort O(n log n).

    Args:
        arr: Lista de elementos comparables.
        reverse: Si True, descendente (usa min-heap).
        inplace: Si True, modifica la lista original.

    Returns:
        Lista ordenada.
    """
    arr = _maybe_copy(arr, inplace)

    def heapify(n: int, i: int):
        """Mantiene la propiedad del heap."""
        extreme = i
        left = 2 * i + 1
        right = 2 * i + 2

        def compare(a, b):
            return (a < b) if reverse else (a > b)

        if left < n and compare(arr[left], arr[extreme]):
            extreme = left
        if right < n and compare(arr[right], arr[extreme]):
            extreme = right

        if extreme != i:
            arr[i], arr[extreme] = arr[extreme], arr[i]
            heapify(n, extreme)

    n = len(arr)

    # Construir heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extraer elementos
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr


# ======================= COUNTING SORT ====================================


def counting_sort(arr: List[int], *, reverse: bool = False) -> List[int]:
    """
    Ordena una lista de enteros usando Counting Sort (O(n + k)).

    IMPORTANTE:
    - Solo funciona con enteros.
    - El rango max-min debe ser razonablemente pequeño.

    Args:
        arr: Lista de enteros.
        reverse: Si True, orden descendente.

    Returns:
        Nueva lista ordenada.
    """
    if not arr:
        return []

    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1

    if range_size > 2_000_000:
        raise ValueError("Counting sort no recomendable para rangos tan grandes.")

    count = [0] * range_size
    output = [0] * len(arr)

    # Contar ocurrencias
    for num in arr:
        count[num - min_val] += 1

    # Suma acumulada
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construcción estable
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output[::-1] if reverse else output


# ======================= BOGO SORT ====================================

def bogo_sort(arr: List[T], *, max_iterations: int = 100000, reverse: bool = False) -> List[T]:
    """
    Ordena una lista usando Bogo Sort (n(∞)).

    Args:
        arr: Lista de elementos comparables.
        max_iterations: Límite para evitar bucles infinitos.
        reverse: Si True, descendente.

    Returns:
        Lista ordenada (si lo logra).
    """
    arr = arr.copy()

    def is_sorted(a):
        return all(a[i] <= a[i + 1] for i in range(len(a) - 1))

    def is_sorted_rev(a):
        return all(a[i] >= a[i + 1] for i in range(len(a) - 1))

    check = is_sorted_rev if reverse else is_sorted

    iterations = 0
    while not check(arr) and iterations < max_iterations:
        random.shuffle(arr)
        iterations += 1

    return arr
