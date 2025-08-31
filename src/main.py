import random
from colorama import Fore, Style, init
from algoritmos import *

init(autoreset=True)

if __name__ == "__main__":

    # Arreglo de números del 0 a n-1
    arreglo = list(range(random.randint(0, 100)))  


    # -------------------------------
    # Configuración: elegir algoritmo
    # -------------------------------
    algoritmo_ejecutar = "busqueda_lineal"


    # Diccionario con todas las funciones disponibles
    funciones = {
        "par_suma_k": lambda: (
            lambda i, j: (
                print(Style.BRIGHT + f"\n{'='*40}"),
                print(Style.BRIGHT+ f" Buscando si existe un par que sume {arreglo[i]+arreglo[j]} "),
                print(f"{'='*40}\n"),
                existe_par_suma_k(arreglo, arreglo[i] + arreglo[j]),
                existe_par_suma_k_optimizado(arreglo, arreglo[i] + arreglo[j]),
            )) (*random.sample(range(len(arreglo)), 2)),
        
        "busqueda_lineal": lambda: (
            lambda valor_buscar, resultado: (
                print(Style.BRIGHT + f"\nBusqueda lineal del valor {valor_buscar}:"),
                print(Fore.GREEN + f"✅ Valor encontrado en índice {resultado[0]}"
                    if resultado[0] != -1 else Fore.RED + f"❌ Valor no encontrado."),
                print(f"Número de comparaciones realizadas: {resultado[1]}\n"),
            )) (valor := random.choice(arreglo), busqueda_lineal(arreglo, valor)),
    }


    # Ejecutar el algoritmo elegido
    if algoritmo_ejecutar in funciones: funciones[algoritmo_ejecutar]()
    else: print(Fore.RED + f"Algoritmo '{algoritmo_ejecutar}' no existe en el compendio.")
