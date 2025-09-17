import random
from colorama import Fore, Style
from algoritmos import *

# -------------------------------
# Funciones para ejecutar los algoritmos
# -------------------------------

def ejecutar_par_suma_k(arreglo):
    i, j = random.sample(range(len(arreglo)), 2)
    k = arreglo[i] + arreglo[j]
    print(Style.BRIGHT + f"\n{'='*40}")
    print(Style.BRIGHT + f" Buscando si existe un par que sume {k} ")
    print(f"{'='*40}\n")
    existe_par_suma_k(arreglo, k)
    existe_par_suma_k_optimizado(arreglo, k)


def ejecutar_busqueda_lineal(arreglo, valor):
    indice, comparaciones = busqueda_lineal(arreglo, valor)
    print(Style.BRIGHT + f"\nBúsqueda lineal del valor {valor}:")
    if indice != -1: print(Fore.GREEN + f"✅ Valor encontrado en índice {indice}")
    else: print(Fore.RED + "❌ Valor no encontrado.")
    print(f"Número de comparaciones realizadas: {comparaciones}\n")


def ejecutar_suma_recursiva(lista):
    print(Style.BRIGHT + f"\nSuma recursiva de la lista {lista}:")
    print(Fore.GREEN + f"Resultado: {suma_recursiva(lista)}\n")


def ejecutar_contar_digitos(n):
    digitos = contar_digitos(n)
    print(Style.BRIGHT + f"\nContar dígitos del número {n}:")
    print(Fore.GREEN + f"Resultado: {digitos}\n")


def ejecutar_eliminar_medio(pila):
    pila_copia = pila.copy()
    print(Style.BRIGHT + f"\nEliminar el elemento medio de la pila {pila_copia}:")
    eliminar_medio(pila_copia)
    print(Fore.GREEN + f"Pila después de eliminar el medio: {pila_copia}\n")


def ejecutar_es_palindromo(cadena):
    print(Style.BRIGHT + f"\nVerificar si la cadena '{cadena}' es un palíndromo:")
    if es_palindromo(cadena): print(Fore.GREEN + "✅ Es un palíndromo.\n")
    else: print(Fore.RED + "❌ No es un palíndromo.\n")
