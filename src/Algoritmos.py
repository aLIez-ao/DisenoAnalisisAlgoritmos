import random
from colorama import Fore, Style


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
