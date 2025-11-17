import random
from algoritmos import *
from runner import *
from utils import *

def main():

    # ============================= Datos de prueba ========================================
    datos = {
        # Números individuales - generados dinámicamente
        "numero_pequeño": lambda: random.randint(1000, 99999),
        "numero_medio": lambda: random.randint(10**8, 10**12),
        "numero_grande": lambda: random.randint(10**30, 10**40),
        
        # Arreglos para ordenamiento - generados dinámicamente
        "arreglo_pequeño": lambda: generar_arreglo(10, -50, 50),
        "arreglo_medio": lambda: generar_arreglo(100, -100, 100),
        "arreglo_grande": lambda: generar_arreglo(1000, -1000, 1000),
        "arreglo_muy_grande": lambda: generar_arreglo(10000, -10000, 10000),
        
        # Listas, pilas y colas
        "lista_aleatoria": lambda: generar_lista(random.randint(50, 150), -100, 100),
        "pila_aleatoria": lambda: generar_pila(random.randint(20, 100), 0, 1000),
        "cola_aleatoria": lambda: generar_cola(random.randint(30, 120), -500, 500),
        
        # Puntos para dominancia
        "puntos_dominancia": lambda: generar_puntos(10, semilla=123),
        
    }

    # ============================= Diccionario de funciones =============================
    funciones = {
        # Dominancia 
        "dominancia_nn": lambda: run_dominancia_nn(datos["puntos_dominancia"]()),
        "dominancia_nlogn": lambda: run_dominancia_nlogn(datos["puntos_dominancia"]()),
        
        # Algoritmos Iterativos
        "suma_digitos_iterativo": lambda: run_suma_digitos_iterativo(datos["numero_grande"]()),
        "mcd_iterativo": lambda: run_mcd_iterativo(datos["numero_grande"](), datos["numero_grande"]()),
        
        # Algoritmos recursivos
        "suma_digitos_recursivo": lambda: run_suma_digitos_recursivo(datos["numero_grande"]()),
        "mcd_recursivo": lambda: run_mcd_recursivo(datos["numero_grande"](), datos["numero_grande"]()),
        
        # Algoritmos de ordenamiento
        "ordenamiento_mergesort": lambda: run_mezcla(),
        "ordenamiento_quicksort": lambda: run_quicksort(),
    }

    # =========================== Ejecutar algoritmo elegido =============================
    algoritmo_ejecutar = "dominancia_nlogn"
    funciones[algoritmo_ejecutar]()
    
   

if __name__ == "__main__":
    main()
        