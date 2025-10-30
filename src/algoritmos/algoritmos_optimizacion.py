"""
Este módulo contiene implementaciones de algoritmos clásicos y optimizados para la resolución de problemas comunes en el análisis y diseño de algoritmos.
Requiere:
- colorama para la salida colorida en consola.
"""
from colorama import Fore, Style
from functools import lru_cache
from typing import List
import math

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


# -------------------------------
# Algoritmos Dinámica optimizados
# -------------------------------

def problema_mochila(valores: list[float], pesos: list[float], capacidad: float, precision: int = 2) -> tuple[float, list[int]]:
    """
    Resuelve el Problema de la Mochila 0/1 con soporte para valores y pesos reales.

    Args:
        valores (list[float]): Lista con los valores de cada ítem.
        pesos (list[float]): Lista con los pesos (pueden ser reales).
        capacidad (float): Capacidad máxima de la mochila (puede ser real).
        precision (int): Número de decimales a conservar al escalar (por defecto 2).

    Returns:
        tuple[float, list[int]]:
            - Valor máximo total que se puede obtener.
            - Lista con los índices de los ítems seleccionados (orden original).
    """
    # Escalamos pesos y capacidad a enteros
    factor = 10**precision
    pesos_int = [int(round(p * factor)) for p in pesos]
    capacidad_int = int(round(capacidad * factor))

    n = len(valores)
    dp = [0.0] * (capacidad_int + 1)
    decision = [[False] * (capacidad_int + 1) for _ in range(n)]

    for i in range(n):
        valor, peso = valores[i], pesos_int[i]
        for w in range(capacidad_int, peso - 1, -1):
            if dp[w] < dp[w - peso] + valor:
                dp[w] = dp[w - peso] + valor
                decision[i][w] = True

    # Reconstrucción de los ítems seleccionados
    items = []
    w = capacidad_int
    for i in range(n - 1, -1, -1):
        if decision[i][w]:
            items.append(i)
            w -= pesos_int[i]

    items.reverse()
    return dp[capacidad_int], items


def problema_agente_viajero(matriz_distancias: list[list[float]],) -> tuple[float, list[int]]:
    """
    Función principal que resuelve el Problema del Agente Viajero.
    """
    numero_ciudades = len(matriz_distancias)
    mascara_completa = masc_completa(numero_ciudades)

    # Convertir lista a tupla para lru_cache
    matriz_tupla = tuple(tuple(fila) for fila in matriz_distancias)

    distancia_total_minima = distancia_min(matriz_tupla, 1, 0, mascara_completa)
    ruta_optima = recons_ruta_optima(matriz_distancias, distancia_min, numero_ciudades)

    return distancia_total_minima, ruta_optima


def masc_completa(numero_ciudades: int) -> int:
    """
    Devuelve la máscara que representa todas las ciudades visitadas.
    """
    return (1 << numero_ciudades) - 1


@lru_cache(maxsize = None)
def distancia_min(matriz_distancias: tuple[tuple[float, ...], ...],conjunto_visitadas: int,ciudad_actual: int,mascara_completa: int,) -> float:
    """
    Calcula recursivamente la distancia mínima para visitar todas las ciudades
    no visitadas desde la ciudad actual.
    """
    if conjunto_visitadas == mascara_completa: return matriz_distancias[ciudad_actual][0]  # Regreso al inicio

    mejor_distancia = math.inf
    numero_ciudades = len(matriz_distancias)

    for siguiente_ciudad in range(numero_ciudades):
        if not (conjunto_visitadas & (1 << siguiente_ciudad)):
            nueva_distancia = matriz_distancias[ciudad_actual][siguiente_ciudad] + distancia_min(
                matriz_distancias,conjunto_visitadas | (1 << siguiente_ciudad), siguiente_ciudad, mascara_completa,)
            mejor_distancia = min(mejor_distancia, nueva_distancia)

    return mejor_distancia


def recons_ruta_optima(matriz_distancias: list[list[float]], funcion_dp, numero_ciudades: int) -> list[int]:
    """
    Reconstruye la ruta óptima a partir de la función de programación dinámica.
    """
    mascara_completa = masc_completa(numero_ciudades)
    conjunto_visitadas: int = 1  # Ciudad inicial visitada
    ciudad_actual: int = 0
    ruta: list[int] = [0]

    matriz_tupla = tuple(tuple(fila) for fila in matriz_distancias)

    while conjunto_visitadas != mascara_completa:
        mejor_ciudad: int | None = None
        mejor_valor: float = math.inf

        for siguiente_ciudad in range(numero_ciudades):
            if not (conjunto_visitadas & (1 << siguiente_ciudad)):
                valor_actual = matriz_distancias[ciudad_actual][siguiente_ciudad] + funcion_dp(
                    matriz_tupla, conjunto_visitadas | (1 << siguiente_ciudad), siguiente_ciudad, mascara_completa,)
                if valor_actual < mejor_valor:
                    mejor_valor = valor_actual
                    mejor_ciudad = siguiente_ciudad

        if mejor_ciudad is not None:
            ruta.append(mejor_ciudad)
            conjunto_visitadas |= 1 << mejor_ciudad
            ciudad_actual = mejor_ciudad

    ruta.append(0)  # Regreso al inicio
    return ruta


def producto_maximo(arreglo: List[int], inicio: int, fin: int) -> float:
    """
    Encuentra el producto máximo de un subarreglo utilizando Divide y Vencerás.
    
    Args:
        arreglo (List[int]): Lista de enteros.
        inicio (int): Índice inicial del subarreglo.
        fin (int): Índice final del subarreglo.
    
    Returns:
        int: Producto máximo dentro del subarreglo arreglo[inicio:fin+1].
    """
    # Caso base: un solo elemento
    if inicio == fin: return arreglo[inicio]
    
    # Dividir el arreglo
    medio = (inicio + fin) // 2
    
    # Producto máximo en la mitad izquierda, derecha y cruzado
    producto_izquierda = producto_maximo(arreglo, inicio, medio)
    producto_derecha = producto_maximo(arreglo, medio + 1, fin)
    producto_cruzado = producto_maximo_cruzado(arreglo, inicio, medio, fin)     
    
    # Retornar el máximo entre los tres
    return max(producto_izquierda, producto_derecha, producto_cruzado) 


def producto_maximo_cruzado(arreglo: List[int], inicio: int, medio: int, fin: int) -> float:
    """
    Calcula el producto máximo que cruza la posición media.
    """
    # Producto hacia la izquierda desde el medio
    producto = 1
    producto_max_izquierda = float('-inf')
    for i in range(medio, inicio - 1, -1):
        producto *= arreglo[i]
        producto_max_izquierda = max(producto_max_izquierda, producto)
    
    # Producto hacia la derecha desde medio+1
    producto = 1
    producto_max_derecha = float('-inf')
    for i in range(medio + 1, fin + 1):
        producto *= arreglo[i]
        producto_max_derecha = max(producto_max_derecha, producto)
    
    # Producto cruzado
    return producto_max_izquierda * producto_max_derecha

