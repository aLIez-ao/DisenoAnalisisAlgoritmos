import sys
import time
import itertools
from typing import List, Dict, Any
from concurrent.futures import ThreadPoolExecutor, Future
from colorama import Fore, Style

from utils import sorting
from algoritmos.benchmarks import measure_sorting_performance

# ============================ CONSTANTES ===============================
_COMPLEXITY_MAP = {
    "bubble_sort": "O(n²)",
    "selection_sort": "O(n²)",
    "insertion_sort": "O(n²)",
    "shell_sort": "O(n^(3/2))",
    "merge_sort": "O(n log n)",
    "quick_sort": "O(n log n)",
    "heap_sort": "O(n log n)",
    "counting_sort": "O(n+k)",
    "bogo_sort": "O((n+1)!)",
}

algoritmos = [
    sorting.bubble_sort,
    sorting.insertion_sort,
    sorting.selection_sort,
    sorting.shell_sort,
    sorting.merge_sort,
    sorting.heap_sort,
    sorting.quick_sort,
    sorting.counting_sort,
]

_SPINNER_CHARS = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

_COL_WIDTH = 10


# ======================= FUNCIONES AUXILIARES (Privadas) ===============

def _get_color_for_time(time_val: float) -> str:
    """Retorna el color de Colorama basado en el umbral de tiempo."""
    if time_val < 0.01: return Fore.GREEN
    if time_val < 1.0:  return Fore.YELLOW
    return Fore.RED


def _pivot_results(raw_results: List[Dict[str, Any]]) -> Dict[str, Dict[int, float]]:
    """
    Transforma la lista plana de resultados en un diccionario anidado.
    Output: { 'quick_sort': { 100: 0.001, 1000: 0.02 }, ... }
    """
    table_data = {}
    for res in raw_results:
        method = res["method"]
        n = res["n"]

        if method not in table_data:
            table_data[method] = {}

        table_data[method][n] = res["time"]
    return table_data


def _run_spinner_animation(future: Future, message: str = "Procesando"):
    """Muestra una animación de carga mientras el Future no haya terminado."""
    spinner = itertools.cycle(_SPINNER_CHARS)

    while future.running():
        sys.stdout.write(
            f"\r{Fore.YELLOW}{next(spinner)} {Fore.CYAN}{message}... {Style.RESET_ALL}"
        )
        sys.stdout.flush()
        time.sleep(0.1)

    # Limpiar línea al terminar
    sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")


def _print_table_header(sizes: List[int]):
    """Imprime la cabecera con ancho fijo calculado."""
    header = f"{'MÉTODO':<20} | {'COMPLEJIDAD':<12}"
    
    for size in sizes:
        # Alineamos "N=..." usando la constante de ancho fijo
        col_title = f"N={size}"
        header += f" | {col_title:<{_COL_WIDTH}}"
    
    print(f"{Fore.WHITE}{Style.BRIGHT}{header}")
    print("-" * len(header))


def _print_algorithm_row(algo_name: str, sizes: List[int], table_data: Dict[str, Dict[int, float]]):
    """Formatea la fila aplicando padding ANTES del color para alinear perfecto."""
    complexity = _COMPLEXITY_MAP.get(algo_name, "???")
    row_str = f"{Fore.BLUE}{algo_name:<20} {Fore.WHITE}| {Fore.MAGENTA}{complexity:<12}"

    # Si el algoritmo fue saltado (ej. bogo)
    if algo_name not in table_data:
        for _ in sizes:
             # Padding manual para el SKIP
             row_str += f" {Fore.WHITE}| {Fore.BLACK}{'SKIP':<{_COL_WIDTH}}"
        print(row_str)
        return

    for size in sizes:
        time_val = table_data[algo_name].get(size, None)
        
        if time_val is None:
            # Caso específico (si falla un solo dato)
            val_str_padded = f"{'SKIP':<{_COL_WIDTH}}"
            colored_val = f"{Fore.BLACK}{val_str_padded}"
        else:
            # 1. Formateamos el numero a string
            time_str = f"{time_val:.5f}s"
            
            # 2. Aplicamos PADDING al texto limpio (sin color aún)
            # Esto garantiza que visualmente ocupe _COL_WIDTH espacios
            time_str_padded = f"{time_str:<{_COL_WIDTH}}"
            
            # 3. Ahora sí aplicamos el color
            color = _get_color_for_time(time_val)
            colored_val = f"{color}{time_str_padded}"
        
        row_str += f" {Fore.WHITE}| {colored_val}"

    print(row_str)


# ========================== FUNCIÓN PRINCIPAL =================================

def run_benchmark(sizes: List[int]):
    """
    Orquestador principal: Configura, ejecuta en hilos, anima y renderiza.
    """
    
    print(
        f"{Fore.CYAN}{Style.BRIGHT}Iniciando Benchmarks para N={sizes}{Style.RESET_ALL}\n"
    )

    # Ejecución Asíncrona (Worker)
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(measure_sorting_performance, algoritmos, sizes)

        # Animación (Main Thread)
        _run_spinner_animation(future, message="Ordenando y midiendo")

        # Obtención de resultados
        try:
            raw_results = future.result()
        except Exception as e:
            print(f"\n{Fore.RED}Error durante el benchmark: {e}")
            return

    # Procesamiento de datos
    pivoted_data = _pivot_results(raw_results)

    # Renderizado
    _print_table_header(sizes)

    for algo in algoritmos:
        _print_algorithm_row(algo.__name__, sizes, pivoted_data)

    print(f"\n{Fore.CYAN}Benchmark finalizado.")
