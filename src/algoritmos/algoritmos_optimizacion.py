"""
Este módulo contiene implementaciones de algoritmos clásicos y optimizados para la resolución de problemas comunes en el análisis y diseño de algoritmos.
Requiere:
- colorama para la salida colorida en consola.
"""

from colorama import Fore, Style

# -------------------------------
# Algoritmos optimizados
# -------------------------------

# Dado un arreglo de n de números enteros y un entero k.
# Determinar si en el arreglo existe un par que dé como suma k.
# A[x]+A[x']=k
def existe_par_suma_k(arreglo, k):
    """
    Algoritmo fuerza bruta: busca si existe un par en 'arreglo' cuya suma sea igual a 'k'.
    Complejidad O(n²)
    """
    n = len(arreglo)

    for i in range(n):
        for j in range(i + 1, n):
            if arreglo[i] + arreglo[j] == k:
                print(
                    Fore.GREEN
                    + f"[Fuerza Bruta] Par encontrado: {arreglo[i]} + {arreglo[j]} = {k}"
                )
                return True

    print(Fore.RED + "[Fuerza Bruta] No se encontró ningún par.")
    return False

def existe_par_suma_k_optimizado(arreglo, k):
    """
    Algoritmo optimizado: utiliza un diccionario para encontrar un par cuya suma sea igual a 'k'.
    Complejidad O(n).
    """
    vistos = {}

    for numero in arreglo:
        complemento = k - numero
        if complemento in vistos:
            print(
                Fore.GREEN
                + f"[Optimizado] Par encontrado: {numero} + {complemento} = {k}"
            )
            return True
        vistos[numero] = True

    print(Fore.RED + "[Optimizado] No se encontró ningún par.")
    return False


# Busqueda líneal. La función debe recibir dos argumentos: el arreglo y el valor a buscar.
# Debe regresar el número de comparaciones realizadas en la búsqueda.
def busqueda_lineal(arreglo, valor):
    """
    Realiza una búsqueda lineal en un arreglo unidimensional de números.

    Parámetros:
        arreglo (list): Lista de números donde se realizará la búsqueda.
        valor (int | float): Valor a buscar en el arreglo.

    Retorna:
        tuple: (indice, comparaciones)
            - indice: posición donde se encontró el valor o -1 si no se encuentra.
            - comparaciones: número total de comparaciones realizadas.
    """
    comparaciones = 0

    for i in range(len(arreglo)):
        comparaciones += 1
        if arreglo[i] == valor:
            return i, comparaciones

    return -1, comparaciones


