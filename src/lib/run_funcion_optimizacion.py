import random
from typing import List, Tuple
from colorama import Fore, Style
from algoritmos import *
from lib import *
from .lector_txt import leer_txt


def run_par_suma_k(arreglo):
    """
    Busca y ejecuta algoritmos para encontrar un par de números en el arreglo
    que sumen un valor k (calculado aleatoriamente a partir de dos elementos).

    Compara dos versiones: la búsqueda estándar y la optimizada.

    Args:
        arreglo (list): Lista de enteros donde se buscarán los pares.

    Returns:
        None. Imprime en consola los resultados de ambas búsquedas.

    Nota:
        - Selecciona aleatoriamente dos índices del arreglo
        - Calcula k como la suma de los elementos en esos índices
        - Ejecuta dos funciones de búsqueda para comparar resultados
    """
    i, j = random.sample(range(len(arreglo)), 2)
    k = arreglo[i] + arreglo[j]
    print(Style.BRIGHT + f"\n{'='*40}")
    print(Style.BRIGHT + f" Buscando si existe un par que sume {k} ")
    print(f"{'='*40}\n")
    existe_par_suma_k(arreglo, k)
    existe_par_suma_k_optimizado(arreglo, k)


def run_busqueda_lineal(arreglo, valor):
    """
    Ejecuta la búsqueda lineal de un valor en el arreglo e imprime
    el resultado con información sobre comparaciones realizadas.

    Args:
        arreglo (list): Lista de enteros donde se realizará la búsqueda.
        valor (int): El valor a buscar en el arreglo.

    Returns:
        None. Imprime en consola el índice encontrado o mensaje de no encontrado,
        junto con el número de comparaciones realizadas.

    Output:
        - Mensaje de éxito en verde si se encuentra el valor
        - Mensaje de error en rojo si no se encuentra
        - Número total de comparaciones realizadas
    """
    indice, comparaciones = busqueda_lineal(arreglo, valor)
    print(Style.BRIGHT + f"\nBúsqueda lineal del valor {valor}:")
    if indice != -1: print(Fore.GREEN + f"✅ Valor encontrado en índice {indice}")
    else: print(Fore.RED + "❌ Valor no encontrado.")
    print(f"Número de comparaciones realizadas: {comparaciones}\n")


def run_problema_mochila(nombres, valores, pesos, capacidad):
    """
    Ejecuta el algoritmo del Problema de la Mochila 0/1 y muestra los resultados en consola.

    Esta función realiza los siguientes pasos:
      1. Imprime la lista de ítems disponibles con sus nombres, valores y pesos.
      2. Calcula la selección óptima de ítems que maximiza el valor total sin exceder
         la capacidad de la mochila, utilizando la función `problema_mochila`.
      3. Muestra los resultados en consola de manera clara, con colores y símbolos:
         - Valor máximo obtenido.
         - Peso total de los ítems seleccionados.
         - Lista de ítems seleccionados, con sus valores y pesos.

    Args:
        nombres (list[str]): Lista con los nombres de los ítems. Sirve para mostrar
                             información legible en consola.
        valores (list[int]): Lista con los valores de cada ítem.
        pesos (list[int]): Lista con los pesos de cada ítem.
        capacidad (int): Peso máximo que la mochila puede contener.

    Returns:
        None: La función no devuelve valores, solo imprime resultados en consola.
    """
    print(Style.BRIGHT + "🎒 Resolución del Problema de la Mochila (0/1)")
    print(Fore.YELLOW + f"Capacidad máxima de la mochila: {capacidad} kg")
    print(Fore.CYAN + "\nItems disponibles:")

    for nombre, valor, peso in zip(nombres, valores, pesos):
        print(f"  - {nombre:<15} (Valor: ${valor}, Peso: {peso} kg)")

    valor_max, indices_items = problema_mochila(valores, pesos, capacidad)
    
    print(Fore.MAGENTA + "\n" + "─" * 45)
    print(Style.BRIGHT + "Resultados de la Optimización:")
    print(Fore.GREEN + f"💰 Valor máximo obtenido: ${valor_max}")

    peso_total = sum(pesos[i] for i in indices_items)
    print(Fore.GREEN + f"⚖️  Peso total en mochila: {peso_total} kg")

    print(Fore.GREEN + "\nItems seleccionados:")
    if not indices_items:
        print("  (Ningún ítem fue seleccionado)")
    else:
        for i in indices_items:
            print(f"  ✅ {nombres[i]:<15} (Valor: ${valores[i]}, Peso: {pesos[i]} kg)")

    print(Fore.MAGENTA + "─" * 45 + "\n")
    

def run_agente_viajero(nombres_ciudades: list[str], matriz_distancias: list[list[float]]):
    """
    Ejecuta el Problema del Agente Viajero (TSP) y muestra los resultados en consola.

    Pasos realizados:
      1. Imprime la lista de ciudades disponibles.
      2. Calcula la ruta óptima que visita todas las ciudades exactamente una vez
         y regresa al inicio, utilizando la función `problema_agente_viajero`.
      3. Muestra la distancia mínima total y el orden de la ruta óptima.

    Args:
        nombres_ciudades (list[str]): Lista con los nombres de las ciudades.
        matriz_distancias (list[list[float]]): Matriz NxN con las distancias entre las ciudades.

    Returns:
        None. La función imprime los resultados en consola.
    """
    numero_ciudades = len(nombres_ciudades)
    print(Style.BRIGHT + "🗺️  Resolución del Problema del Agente Viajero (TSP)")
    print(Fore.CYAN + f"Ciudades disponibles ({numero_ciudades}):")
    for i, nombre in enumerate(nombres_ciudades):
        print(f"  - {nombre} (Índice: {i})")

    # Ejecutar algoritmo
    distancia_minima, ruta_optima = problema_agente_viajero(matriz_distancias)

    # Mostrar resultados
    print(Fore.MAGENTA + "\n" + "─" * 50)
    print(Style.BRIGHT + "Resultados de la Optimización:")
    print(Fore.GREEN + f"📏 Distancia mínima total del recorrido: {distancia_minima:.2f}")

    print(Fore.GREEN + "\nRuta óptima encontrada:")
    ruta_nombres = [nombres_ciudades[i] for i in ruta_optima]
    print("  ➤ " + " → ".join(ruta_nombres))

    print(Fore.MAGENTA + "─" * 50 + "\n")
    
    
def run_producto_maximo_visual(arreglo: List[int], inicio: int, fin: int) -> float:
    """
        Encuentra el producto máximo de un subarreglo y lo pinta en consola.
        
        Args:
            arreglo (List[int]): Lista de enteros.
            inicio (int): Índice inicial del subarreglo.
            fin (int): Índice final del subarreglo.
        
        Returns:
            float: Producto máximo dentro del subarreglo.
        """
        # Caso base
    if inicio == fin:
        print(f"{Fore.CYAN}Subarreglo [{inicio}:{fin}] → único elemento: {arreglo[inicio]}")
        return arreglo[inicio]

    medio = (inicio + fin) // 2

    print(f"{Fore.YELLOW}Dividiendo subarreglo [{inicio}:{fin}] en [{inicio}:{medio}] y [{medio+1}:{fin}]")

    producto_izquierda = run_producto_maximo_visual(arreglo, inicio, medio)
    producto_derecha = run_producto_maximo_visual(arreglo, medio + 1, fin)
    producto_cruzado = producto_maximo_cruzado_visual(arreglo, inicio, medio, fin)

    producto_max = max(producto_izquierda, producto_derecha, producto_cruzado)
    print(f"{Fore.MAGENTA}Producto máximo en subarreglo [{inicio}:{fin}] → {Fore.GREEN}{producto_max}\n")
        
    return producto_max

def producto_maximo_cruzado_visual(arreglo: List[int], inicio: int, medio: int, fin: int) -> float:
    """
    Calcula el producto máximo cruzando la mitad y lo muestra en consola.
    """
    producto = 1
    producto_max_izquierda = float('-inf')
    for i in range(medio, inicio - 1, -1):
        producto *= arreglo[i]
        producto_max_izquierda = max(producto_max_izquierda, producto)
    print(f"  {Fore.BLUE}Máximo hacia la izquierda desde medio {medio}: {producto_max_izquierda}")

    producto = 1
    producto_max_derecha = float('-inf')
    for i in range(medio + 1, fin + 1):
        producto *= arreglo[i]
        producto_max_derecha = max(producto_max_derecha, producto)
    print(f"  {Fore.BLUE}Máximo hacia la derecha desde medio {medio+1}: {producto_max_derecha}")

    producto_cruzado = producto_max_izquierda * producto_max_derecha
    print(f"  {Fore.YELLOW}Producto cruzado [{inicio}:{fin}]: {Fore.GREEN}{producto_cruzado}")
    return producto_cruzado