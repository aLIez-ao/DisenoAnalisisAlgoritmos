import random
from pathlib import Path
from algoritmos import matriz_distancias
from lib import *

if __name__ == "__main__":
    
    # -------------------------------
    # Generar datos de prueba
    # -------------------------------

    # Estructuras aleatorias - generadas dinámicamente
    n = random.randint(1, 1000)
    arreglo = generar_arreglo(1000, -100, 100)
    lista = generar_lista(random.randint(50, 150), -100, 100)
    pila = generar_pila(random.randint(20, 100), 0, 1000)
    cola = generar_cola(random.randint(30, 120), -500, 500)

    # Datos individuales
    palindromo = "anita lava la tina"
    ESP = "abcdefghijklmnñopqrstuvwxyz ,."
    ruta = "resources/texto.txt"

    # Problema de la mochila
    items = [f"Item {i+1}" for i in range(10)]
    len_items = len(items)
    valores = generar_arreglo(len_items, 50, 500)
    pesos = generar_arreglo(len_items, 0, 10, True)
    mochila = n / 2

    # Problema del agente viajero
    ciudades = [f"Ciudad {i+1}" for i in range(5)]
    len_cuidades = len(ciudades)
    matriz = [[0 if i == j else random.randint(10, 50) for j in range(len_cuidades)] for i in range(len_cuidades)]
    distancias = matriz_distancias(matriz)

    
    # -------------------------------
    # Diccionario de funciones
    # -------------------------------
    funciones = {
        # Algoritmos optimizados
        "par_suma_k": lambda: run_par_suma_k(arreglo),
        "busqueda_lineal": lambda: run_busqueda_lineal(arreglo, random.choice(arreglo)),
        "mochila": lambda: run_problema_mochila(items, valores, pesos, mochila),
        "viajero": lambda: run_agente_viajero(ciudades, distancias),
        "producto_maximo": lambda: run_producto_maximo_visual(arreglo, 0, len(arreglo)-1),
        
        # Algoritmos recursivos
        "suma": lambda: run_suma_recursiva(lista),
        "contar_digitos": lambda: run_contar_digitos(n),
        "eliminar_medio": lambda: run_eliminar_medio(pila),
        "palindromo": lambda: run_es_palindromo(palindromo),
        
        # Algoritmos de fuerza bruta
        "maximo_producto": lambda: run_maximo_producto(arreglo),
        "cifrar_cesar": lambda: run_cifrar_cesar(ruta, n, ESP),
        "descifrar_cesar": lambda: run_descifrar_cesar(ruta, ESP),
        "descifrar_cesar_tex": lambda: run_cifrar_decifrar_cesar(ruta, 3, ESP),
        
        # Algoritmos de ordenamiento
        "mergesort": lambda: run_mergesort(arreglo),
        "quicksort": lambda: run_quicksort(arreglo),
    }

    # -------------------------------
    # Ejecutar algoritmo elegido
    # -------------------------------
    algoritmo_ejecutar = "mochila"
    funciones[algoritmo_ejecutar]()
