from utils import *
from typing import  Dict, Any

def print_results_table(data: Dict[str, Any]):
    """
    Imprime los resultados de las mediciones en una tabla formateada.

    En lugar de "Big O en la última fila" (lo cual es ambiguo con
    columnas de datos), se añade como la última columna, que es
    la forma estándar y más clara de presentar esta información.
    
    Args:
        data: El diccionario de resultados devuelto por measure_sorting_times.
    """
    results = data["results"]
    algorithms = data["algorithms"]
    sizes = data["sizes"]
    big_o_map = data["big_o"]

    # Calcular anchos de columna
    
    # Ancho de la primera columna (Nombres de algoritmos)
    col_width_alg = len("Algoritmo")
    for name, _ in algorithms:
        col_width_alg = max(col_width_alg, len(name))
    
    # Ancho de la última columna (Big O)
    col_width_big_o = len("Big O")
    for complexity in big_o_map.values():
        col_width_big_o = max(col_width_big_o, len(complexity))

    # Ancho de las columnas de datos (10, 100, 1000...)
    col_widths_sizes = {}
    for size in sizes:
        # El ancho es el máximo entre el título (ej: "10000") y los datos
        header_width = len(str(size))
        max_data_width = 0
        for name, _ in algorithms:
            result_val = results[name][size]
            if isinstance(result_val, float):
                formatted_val = f"{result_val:.6f}s"
            else:
                formatted_val = str(result_val) # "N/A" o "Error"
            max_data_width = max(max_data_width, len(formatted_val))
        
        col_widths_sizes[size] = max(header_width, max_data_width)

    # Imprimir Encabezado
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

    # Imprimir Filas de Datos
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
