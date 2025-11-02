"""
Módulo: algoritmos_ordenamiento

Este módulo contiene implementaciones de algoritmos de ordenamiento en Python.

Cada función recibe una lista de elementos comparables y devuelve la lista
ordenada (ya sea como una nueva lista o modificando la original en el caso de
las versiones iterativas in-place).
"""
import random

def ordenamiento_mezcla(arreglo):
    """
    Implementación del algoritmo de ordenamiento por mezcla (Merge Sort).

    Parámetro:
    arreglo: Una lista de elementos comparables.

    Retorno:
    list: Una nueva lista con los elementos de 'arreglo' ordenados.
    """
    # Caso base
    if len(arreglo) <= 1: return arreglo

    mid = len(arreglo) // 2
    izquierda = ordenamiento_mezcla(arreglo[:mid])
    derecha = ordenamiento_mezcla(arreglo[mid:])

    # Merge de las dos listas ordenadas
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agrega los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


def ordenamiento_mezcla_iterativo(arreglo):
    """
    Implementación iterativa (no recursiva) de Merge Sort.

    Parámetro:
    arr (list): Una lista de elementos comparables.

    Retorno:
    list: La lista 'arr' ordenada en su lugar.
    """
    length = len(arreglo)
    longitud = 1  # Tamaño inicial de sublistas a fusionar

    # Arreglo temporal para mezcla
    temp = [0] * length

    while longitud < length:
        inicio = 0
        while inicio < length:
            medio = min(inicio + longitud - 1, length - 1)
            fin = min(inicio + 2 * longitud - 1, length - 1)

            # Índices para fusionar
            a = inicio       # puntero mitad izquierda
            b = medio + 1    # puntero mitad derecha
            c = inicio       # puntero de temp

            # Mezclar las dos mitades
            while a <= medio and b <= fin:
                if arreglo[a] <= arreglo[b]:
                    temp[c] = arreglo[a]
                    a += 1
                else:
                    temp[c] = arreglo[b]
                    b += 1
                c += 1

            # Copiar elementos restantes de la mitad izquierda
            while a <= medio:
                temp[c] = arreglo[a]
                a += 1
                c += 1

            # Copiar elementos restantes de la mitad derecha
            while b <= fin:
                temp[c] = arreglo[b]
                b += 1
                c += 1

            # Copiar de temp de vuelta a arreglo
            for i in range(inicio, fin + 1): arreglo[i] = temp[i]
            inicio += 2 * longitud
        longitud *= 2

    return arreglo


def ordenamiento_quicksort(arreglo):
    """
    Implementación del algoritmo de ordenamiento rápido (Quicksort).

    Parámetro:
    arreglo: Una lista de elementos comparables.

    Retorno:
    list: Una nueva lista con los elementos de 'arreglo' ordenados.
    """
    # Caso base
    if len(arreglo) <= 1: return arreglo

    # Selección de pivote aleatorio para evitar peor caso
    pivote = arreglo[random.randint(0, len(arreglo) - 1)]

    # Partición en menores, iguales y mayores
    menores = [x for x in arreglo if x < pivote]
    iguales = [x for x in arreglo if x == pivote]
    mayores = [x for x in arreglo if x > pivote]

    # Recursión y combinación
    return ordenamiento_quicksort(menores) + iguales + ordenamiento_quicksort(mayores)
    

def ordenamiento_quicksort_iterativo(arreglo):
    """
    Ordenamiento rápido (Quicksort) iterativo.
    
    Parámetro:
    arreglo (list): Lista de elementos comparables.
    
    Retorno:
    list: Lista 'arreglo' ordenada en su lugar.
    """
    n = len(arreglo)
    # Pila para almacenar subarreglos a ordenar: (inicio, fin)
    pila = [(0, n - 1)]

    while pila:
        inicio, fin = pila.pop()

        if inicio >= fin: continue  # Subarreglo de 0 o 1 elemento, ya ordenado

        # Elegir pivote (último elemento del subarreglo)
        pivote = arreglo[fin]
        izq = inicio - 1

        # Partición
        for der in range(inicio, fin):
            if arreglo[der] <= pivote:
                izq += 1
                arreglo[izq], arreglo[der] = arreglo[der], arreglo[izq]

        # Colocar el pivote en su posición correcta
        arreglo[izq + 1], arreglo[fin] = arreglo[fin], arreglo[izq + 1]
        indice_pivote = izq + 1

        # Agregar subarreglos a la pila
        # Procesar subarreglos más grandes primero para minimizar profundidad de pila
        if indice_pivote + 1 < fin: pila.append((indice_pivote + 1, fin))
        if indice_pivote - 1 > inicio: pila.append((inicio, indice_pivote - 1))

    return arreglo
