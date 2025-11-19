import time
import os
from typing import List, Optional, Tuple
from colorama import Fore, Style
from runner import log_debug, Spinner
from utils.io_handlers import read_campo_file, write_campo_file, Point
from utils.visualizer import plot_triangle_solution
from algoritmos.max_area_triangle import solve_optimized, solve_brute_force

# Alias de Tipo para que el código sea más legible
Triangle = Tuple[Point, Point, Point]


# ====================== FUNCIONES AUXILIARES =============================

def _load_and_validate_points(filepath: str) -> Optional[List[Point]]:
    """Carga los puntos y verifica condiciones mínimas."""
    if not os.path.exists(filepath):
        print(f"{Fore.RED}Error: No se encontró {filepath}{Style.RESET_ALL}")
        return None

    points = read_campo_file(filepath)
    n = len(points)
    print(f"Puntos cargados: {Fore.YELLOW}{n}{Style.RESET_ALL}")
    
    if n < 3:
        print(f"{Fore.RED}Error: Se necesitan al menos 3 puntos.{Style.RESET_ALL}")
        return None
        
    log_debug(f"Primeros 3 puntos: {points[:3]}...")
    return points


def _run_optimized_strategy(points: List[Point]) -> Triangle:
    """Ejecuta y mide la solución optimizada (Convex Hull)."""
    print(f"\n{Fore.BLUE}Ejecutando Solución Optimizada{Style.RESET_ALL}")
    
    start = time.perf_counter()
    best_triangle = solve_optimized(points)
    elapsed = time.perf_counter() - start
    
    print(f"Tiempo: {Fore.GREEN}{elapsed:.6f}s{Style.RESET_ALL}")
    return best_triangle


def _validate_with_brute_force(points: List[Point], optimized_result: Triangle):
    """Ejecuta fuerza bruta y compara resultados. Si N es pequeño."""
    n = len(points)
    
    # Límite para evitar congelar la PC
    if n > 500:
        print(f"\n{Fore.YELLOW}Saltando Fuerza Bruta: N={n} es muy grande para O(n^3).{Style.RESET_ALL}")
        return

    print(f"\n{Fore.MAGENTA}Ejecutando Fuerza Bruta (Validación){Style.RESET_ALL}")
    
    best_triangle_brute = None
    elapsed = 0

    with Spinner("Validando algoritmos"):
        start = time.perf_counter()
        best_triangle_brute = solve_brute_force(points)
        elapsed = time.perf_counter() - start

    print(f"Tiempo: {Fore.RED}{elapsed:.6f}s{Style.RESET_ALL}")

    # Comparación usando conjuntos (el orden de los vértices no importa)
    if set(optimized_result) == set(best_triangle_brute):
        print(f"{Fore.GREEN}VALIDACIÓN EXITOSA: Resultados idénticos.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}ERROR: Los resultados difieren.{Style.RESET_ALL}")
        log_debug(f"Opt: {optimized_result} | Brute: {best_triangle_brute}")


def _visualize_results(points: List[Point], triangle: Triangle):
    """Maneja la visualización gráfica con Matplotlib."""
    print(f"\n{Fore.MAGENTA}Generando gráfico de resultados{Style.RESET_ALL}")
    
    # El spinner girará mientras Matplotlib carga la ventana.
    # Nota: plot_triangle_solution bloquea, así que el spinner se detendrá
    # visualmente cuando la ventana aparezca o se cierre, dependiendo del backend.
    with Spinner("Matplotlib abrierto"):
        plot_triangle_solution(points, triangle)


# ============================= FUNCIÓN PRINCIPAL =================================

def run_triangle_challenge(input_file: str = "resources/campo.in", output_file: str = "resources/campo.out"):
    """
    Orquesta el flujo completo de resolución para el desafío del Triángulo de Área Máxima.

    Esta función actúa como el controlador principal (Driver), integrando los módulos 
    de E/S, lógica algorítmica y visualización. Sigue el siguiente pipeline secuencial:

    1. **Carga (ETL):** Lee y valida los puntos desde `input_file`.
    2. **Procesamiento:** Ejecuta la estrategia optimizada (Convex Hull + Search).
    3. **Validación (Benchmark):** Si N <= 500, ejecuta Fuerza Bruta para verificar 
       la corrección matemática y comparar tiempos de ejecución.
    4. **Persistencia:** Escribe las coordenadas del triángulo ganador en `output_file`.
    5. **Visualización:** Genera un gráfico interactivo con Matplotlib mostrando 
       la nube de puntos, el perímetro convexo y la solución.

    Parámetros
    ----------
    input_file : str, opcional
        Ruta relativa o absoluta al archivo de texto con las coordenadas.
        Debe terminar con la línea sentinel "-1 -1". 
        Por defecto es "resources/campo.in".
    
    output_file : str, opcional
        Ruta de destino donde se guardarán las coordenadas de los 3 vértices solución.
        Por defecto es "resources/campo.out".

    Retorna
    -------
    None
        Esta función no retorna valores; opera puramente a través de efectos 
        secundarios (impresión en consola, escritura en disco y ventanas gráficas).
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}Triángulo de Área Máxima{Style.RESET_ALL}")

    # Lectura
    points = _load_and_validate_points(input_file)
    if not points: return

    # Ejecución Principal
    best_triangle = _run_optimized_strategy(points)

    # Validación
    _validate_with_brute_force(points, best_triangle)

    # Persistencia
    write_campo_file(output_file, best_triangle)
    log_debug(f"Triángulo maximizado: {best_triangle}")
    print(f"\n{Fore.CYAN}Resultado guardado en {output_file}{Style.RESET_ALL}")
    
    # Visualización
    _visualize_results(points, best_triangle)
