import random
from lib import *


if __name__ == "__main__":

    n = random.randint(1, 100)
    arreglo = generar_arreglo(5)
    lista = generar_lista(n)
    pila = generar_pila(n)
    texto = "anita lava la tina"
    ruta = lector_txt.leer_txt(r"resources\texto.txt")
    # ruta = r"resources\hola_mundo.txt"

    ESP = "abcdefghijklmnñopqrstuvwxyz ,."

    items = ["Laptop", "Libro", "Botella de Agua", "Cámara", "Snack", "Tablet"]
    valores_items = [500, 150, 80, 300, 60, 400]
    pesos_items = [3.5, 1.3, 1, 2.5, 0.5, 2]
    capacidad_mochila = 10

    nombres_ciudades = ["Ciudad A", "Ciudad B", "Ciudad C", "Ciudad D"]
    matriz_distancias_int = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    matriz_distancias = [[float(x) for x in fila] for fila in matriz_distancias_int]

    # -------------------------------
    # Diccionario de funciones
    # -------------------------------
    funciones = {
        # Algoritmos optimizados
        "par_suma_k": lambda: ejecutar_par_suma_k(arreglo),
        "busqueda_lineal": lambda: ejecutar_busqueda_lineal(arreglo, random.choice(arreglo)),
        "problema_mochila": lambda: ejecutar_problema_mochila(items, valores_items, pesos_items, capacidad_mochila),
        "problema_agente_viajero": lambda: ejecutar_agente_viajero(nombres_ciudades, matriz_distancias),
        "producto_maximo_visual": lambda: ejecutar_producto_maximo_visual(arreglo, 0, len(arreglo)-1),
        
        # Algoritmos recursivos
        "suma_recursiva": lambda: ejecutar_suma_recursiva(lista),
        "contar_digitos": lambda: ejecutar_contar_digitos(n),
        "eliminar_medio": lambda: ejecutar_eliminar_medio(pila),
        "es_palindromo": lambda: ejecutar_es_palindromo(texto),
        
        # Algoritmos de fuerza bruta
        "maximo_producto": lambda: ejecutar_maximo_producto(arreglo),
        "cifrar_cesar": lambda: ejecutar_cifrar_cesar(ruta, n, ESP),
        "descifrar_cesar": lambda: ejecutar_descifrar_cesar(ruta, ESP),
        "ejecutar_cifrar_cesar_texto": lambda: ejecutar_cifrar_decifrar_cesar(ruta, 3, ESP),
        
        # Algoritmos de ordenamiento
        "ordenamiento_mergesort": lambda: ejecutar_mergesort(arreglo),
        "ordenamiento_quicksort": lambda: ejecutar_quicksort(arreglo),
    }

    # -------------------------------
    # Ejecutar algoritmo elegido
    # -------------------------------
    algoritmo_ejecutar = "producto_maximo_visual"
    funciones[algoritmo_ejecutar]()
