import random
from ejecutar_funcion import *


if __name__ == "__main__":

    # Datos de ejemplo
    n = random.randint(1, 100)
    arreglo = list(range(1, n + 1))
    lista = list(range(1, n + 1))
    pila = list(range(1, n + 1))
    cadena = "anita lava la tina"

    # -------------------------------
    # Diccionario de funciones
    # -------------------------------
    funciones = {
        # Algoritmos optimizados
        "par_suma_k": lambda: ejecutar_par_suma_k(arreglo),
        "busqueda_lineal": lambda: ejecutar_busqueda_lineal(arreglo, random.choice(arreglo)),
        
        # Algoritmos recursivos
        "suma_recursiva": lambda: ejecutar_suma_recursiva(lista),
        "contar_digitos": lambda: ejecutar_contar_digitos(n),
        "eliminar_medio": lambda: ejecutar_eliminar_medio(pila),
        "es_palindromo": lambda: ejecutar_es_palindromo(cadena),
    }

    # -------------------------------
    # Ejecutar algoritmo elegido
    # -------------------------------
    algoritmo_ejecutar = "contar_digitos"
    funciones[algoritmo_ejecutar]()