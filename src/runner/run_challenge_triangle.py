import time
import os
from colorama import Fore, Style
from runner import log_debug
from utils.io_handlers import *
from utils.visualizer import *
from algoritmos.max_area_triangle import *

def run_triangle_challenge(input_file: str = "resources/campo.in", output_file: str = "resources/campo.out"):
    
    print(f"{Fore.CYAN}{Style.BRIGHT}=== Desafío Triángulo de Área Máxima ==={Style.RESET_ALL}")

    # Lectura
    if not os.path.exists(input_file):
        print(f"{Fore.RED}Error: No se encontró {input_file}{Style.RESET_ALL}")
        return

    points = read_campo_file(input_file)
    n = len(points)
    print(f"Puntos cargados: {Fore.YELLOW}{n}{Style.RESET_ALL}")
    log_debug(f"Primeros 3 puntos: {points[:3]}...")

    if n < 3:
        print(f"{Fore.RED}Error: Se necesitan al menos 3 puntos.{Style.RESET_ALL}")
        return

    
    # --------------- Método 1: Optimizado ------------------------------------------------
    print(f"\n{Fore.BLUE}Ejecutando Solución Optimizada (Convex Hull)...{Style.RESET_ALL}")
    start = time.perf_counter()
    best_triangle_opt = solve_optimized(points)
    time_opt = time.perf_counter() - start
    print(f"Tiempo: {Fore.GREEN}{time_opt:.6f}s{Style.RESET_ALL}")

    # --------------- Método 2: Fuerza Bruta (Solo para validar/benchmark) ---------------
    if n <= 500: 
        print(f"\n{Fore.MAGENTA}Ejecutando Fuerza Bruta (Validación)...{Style.RESET_ALL}")
        start = time.perf_counter()
        best_triangle_brute = solve_brute_force(points)
        time_brute = time.perf_counter() - start
        print(f"Tiempo: {Fore.RED}{time_brute:.6f}s{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}Saltando Fuerza Bruta (N muy grande).{Style.RESET_ALL}")
        best_triangle_brute = best_triangle_opt

    # Escritura
    log_debug(f"Triángulo ganador: {best_triangle_opt}")
    write_campo_file(output_file, best_triangle_opt)
    print(f"\n{Fore.CYAN}Resultado guardado en {output_file}{Style.RESET_ALL}")
    
    
    print(f"\n{Fore.MAGENTA}Generando gráfico de resultados...{Style.RESET_ALL}")
    
    plot_triangle_solution(points, best_triangle_opt)
