import timeit
import random
import sys  # Necesario para la barra de progreso
import io   # Necesario para silenciar stdout
from typing import List, Callable, Dict, Any, Tuple

# (AQUÍ VAN TODAS TUS FUNCIONES DE ORDENAMIENTO: bubble_sort, merge_sort, ...)

# ===================================================================
# ============== FUNCIÓN AUXILIAR: BARRA DE PROGRESO ================
# ===================================================================

def _print_progress(percentage: float, bar_length: int = 40):
    """Imprime una barra de progreso en la consola que se sobrescribe."""
    filled_length = int(bar_length * percentage / 100)
    bar = '*' * filled_length + ' ' * (bar_length - filled_length)
    # \r = carriage return (volver al inicio de la línea)
    # end="" = no añadir un salto de línea
    sys.stdout.write(f"\r    └─ Progreso: [{bar}] {percentage:6.2f}% completado   ")
    sys.stdout.flush()

# ===================================================================
# ============== FUNCIÓN 1: MEDIR TIEMPOS (ACTUALIZADA) =============
# ===================================================================

def measure_sorting_times(
    algorithms_to_test: List[Tuple[str, Callable]],
    sizes_to_test: List[int]
) -> Dict[str, Any]:
    """
    Mide el tiempo de ejecución de varios algoritmos de ordenamiento.

    Ahora incluye una barra de progreso por método y suprime
    la salida de consola (ej. advertencias de Bogo Sort) durante la medición.
    """
    
    big_o_map = {
        "Bubble Sort": "O(n^2)",
        "Selection Sort": "O(n^2)",
        "Insertion Sort": "O(n^2)",
        "Shell Sort": "O(n^2)",
        "Merge Sort": "O(n log n)",
        "Quick Sort": "O(n log n)",
        "Heap Sort": "O(n log n)",
        "Counting Sort": "O(n + k)",
        "Bogo Sort": "O((n+1)!)"
    }
    
    N_SQUARED_CAP = 10000
    BOGO_CAP = 10
    SLOW_ALGORITHMS = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Shell Sort"]
    
    results: Dict[str, Dict[int, Any]] = {}
    total_sizes = len(sizes_to_test)

    print("Iniciando mediciones... (esto puede tardar varios segundos)")

    for name, func in algorithms_to_test:
        results[name] = {}
        print(f"  Probando: {name}...")

        for i, size in enumerate(sizes_to_test):
            
            # --- Aplicar límites de seguridad ---
            if (name == "Bogo Sort" and size > BOGO_CAP) or \
               (name in SLOW_ALGORITHMS and size > N_SQUARED_CAP):
                
                results[name][size] = "N/A"
                
                # Actualizar progreso y continuar
                percentage = ((i + 1) / total_sizes) * 100
                _print_progress(percentage)
                continue # Ir al siguiente tamaño

            # --- Generar datos de prueba ---
            if name == "Counting Sort":
                test_data = [random.randint(0, 1000) for _ in range(size)]
            else:
                test_data = [random.randint(0, size) for _ in range(size)]
            
            # --- Medir el tiempo (CON SUPRESIÓN DE STDOUT) ---
            old_stdout = sys.stdout  # Guardar la salida estándar original
            sys.stdout = io.StringIO() # Redirigir stdout a un búfer temporal
            
            try:
                number_of_runs = 100 if size <= 100 else 1
                
                time_taken = timeit.timeit(
                    lambda: func(test_data.copy()),
                    number=number_of_runs
                ) / number_of_runs
                
                results[name][size] = time_taken
            
            except Exception as e:
                sys.stdout = old_stdout # Asegurarse de restaurar stdout en caso de error
                print(f"    ERROR en {name} con tamaño {size}: {e}")
                results[name][size] = "Error"
            
            finally:
                sys.stdout = old_stdout # ¡Restaurar siempre la salida estándar!

            # --- Actualizar progreso ---
            percentage = ((i + 1) / total_sizes) * 100
            _print_progress(percentage)
        
        # Imprimir un salto de línea para terminar la barra de progreso
        sys.stdout.write("\n")

    print("Mediciones completadas.\n")
    
    return {
        "results": results,
        "algorithms": algorithms_to_test,
        "sizes": sizes_to_test,
        "big_o": big_o_map
    }

# ===================================================================
# ============== FUNCIÓN 2: IMPRIMIR TABLA (SIN CAMBIOS) ============
# ===================================================================

def print_results_table(data: Dict[str, Any]):
    """
    Imprime los resultados de las mediciones en una tabla formateada.
    (Esta función no necesita cambios)
    """
    results = data["results"]
    algorithms = data["algorithms"]
    sizes = data["sizes"]
    big_o_map = data["big_o"]

    # --- 1. Calcular anchos de columna ---
    col_width_alg = len("Algoritmo")
    for name, _ in algorithms:
        col_width_alg = max(col_width_alg, len(name))
    
    col_width_big_o = len("Big O")
    for complexity in big_o_map.values():
        col_width_big_o = max(col_width_big_o, len(complexity))

    col_widths_sizes = {}
    for size in sizes:
        header_width = len(str(size))
        max_data_width = 0
        for name, _ in algorithms:
            result_val = results[name][size]
            if isinstance(result_val, float):
                formatted_val = f"{result_val:.6f}s"
            else:
                formatted_val = str(result_val)
            max_data_width = max(max_data_width, len(formatted_val))
        col_widths_sizes[size] = max(header_width, max_data_width)

    # --- 2. Imprimir Encabezado ---
    header = f"{'Algoritmo':<{col_width_alg}} | "
    separator = "-" * col_width_alg + "-+-"
    for size in sizes:
        width = col_widths_sizes[size]
        header += f"{str(size):>{width}} | "
        separator += "-" * width + "-+-"
    header += f"{'Big O':<{col_width_big_o}}"
    separator += "-" * col_width_big_o

    print("📊 Tabla de Rendimiento de Algoritmos de Ordenamiento")
    print(header)
    print(separator)

    # --- 3. Imprimir Filas de Datos ---
    for name, _ in algorithms:
        row = f"{name:<{col_width_alg}} | "
        for size in sizes:
            width = col_widths_sizes[size]
            result_val = results[name][size]
            if isinstance(result_val, float):
                formatted_val = f"{result_val:.6f}s"
            else:
                formatted_val = str(result_val)
            row += f"{formatted_val:>{width}} | "
        big_o = big_o_map[name]
        row += f"{big_o:<{col_width_big_o}}"
        print(row)

# ===================================================================
# ============== BLOQUE PRINCIPAL DE EJECUCIÓN ======================
# ===================================================================
