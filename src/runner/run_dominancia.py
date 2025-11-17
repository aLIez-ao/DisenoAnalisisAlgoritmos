import numpy as np
from colorama import Fore, Style
from typing import List, Tuple
from algoritmos.dominancia import *
from utils.visualizacion import *



# ==================== Runner Publicas ================================

def run_dominancia_nlogn(datos: List[Tuple[float, float]]):
    # Ejecutar Algoritmo
    resultados = dominancia_nlogn(datos)
    
    # Imprimir Reporte
    _imprimir_reporte_detallado("Dominancia (Divide & Conquer - N log N)", resultados)
    
    # Visualizar
    print(f"{Fore.MAGENTA}Generando gráfico... (Cierra la ventana para continuar)")
    visualizar_puntos(datos, resultados)
    
    
def run_dominancia_nn(datos: List[Tuple[float, float]]):
    # Ejecutar Algoritmo
    resultados = dominancia_nn(datos)
    
    # Imprimir Reporte
    _imprimir_reporte_detallado("Dominancia (Fuerza Bruta - N^2)", resultados)
    
    # Visualizar
    print(f"{Fore.MAGENTA}Generando gráfico... (Cierra la ventana para continuar)")
    visualizar_puntos(datos, resultados)
    
    
# ==================== Funciones Privadas ================================

def _imprimir_reporte_detallado(nombre_algoritmo: str, resultados: list):
    """
    Función auxiliar para generar una tabla bonita y estadísticas usando Numpy.
    """
    n = len(resultados)
    
    # 1. Encabezado con estilo
    print(f"\n{Style.BRIGHT}{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN} EJECUTANDO: {nombre_algoritmo.upper()}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    # 2. Extraer rangos para análisis con Numpy
    # Estructura resultado: [x, y, id, rango]
    lista_rangos = [fila[3] for fila in resultados]
    arr_rangos = np.array(lista_rangos)
    
    # Estadísticas básicas con Numpy
    promedio = np.mean(arr_rangos)
    max_dom = np.max(arr_rangos)
    optimos = np.sum(arr_rangos == 0) # Cuántos tienen rango 0
    
    print(f"{Fore.YELLOW}--- Resumen Estadístico ---")
    print(f"Total Puntos:      {Style.BRIGHT}{n}")
    print(f"Puntos Óptimos:    {Style.BRIGHT}{Fore.GREEN}{optimos} {Style.RESET_ALL}(Rango 0 - Frontera de Pareto)")
    print(f"Rango Promedio:    {promedio:.2f}")
    print(f"Peor Rango:        {Fore.RED}{max_dom}")
    print(f"{'-'*60}")

    # 3. Tabla de Datos
    print(f"{Style.BRIGHT}{'ID':<5} | {'Coordenadas (X, Y)':<20} | {'Rango':<5} | {'Estado'}")
    print(f"{'-'*60}")

    # Ordenamos por ID para que la tabla se vea ordenada P0, P1, P2...
    resultados_ordenados = sorted(resultados, key=lambda x: x[2])

    for r in resultados_ordenados:
        x, y, id_orig, rango = r
        
        # Coloreado condicional
        if rango == 0:
            # Verde para los ganadores (Pareto)
            color_fila = Fore.GREEN + Style.BRIGHT
            estado = "OPTIMO"
        elif rango == max_dom:
            # Rojo para los más dominados
            color_fila = Fore.RED
            estado = "CRITICO"
        else:
            # Normal para el resto
            color_fila = Fore.RESET
            estado = "-"

        # Imprimir fila formateada
        coord_str = f"({x:>6.2f}, {y:>6.2f})"
        print(f"{color_fila}{f'P{id_orig}':<5} | {coord_str:<20} | {rango:<5} | {estado}")

    print(f"{Style.BRIGHT}{Fore.CYAN}{'='*60}\n")

