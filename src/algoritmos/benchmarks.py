import time
from typing import List, Callable, Dict, Any
from utils.data_generator import lista

def measure_sorting_performance(
    algorithms: List[Callable], 
    sizes: List[int]
) -> List[Dict[str, Any]]:
    """
    Ejecuta benchmarks para una lista de algoritmos y tamaños de datos.
    
    Returns:
        Lista de diccionarios con keys: 'method', 'n', 'time'.
    """
    results = []

    for n in sizes:
        # Generamos la lista base una sola vez por tamaño
        original_data = lista(n)
        
        for sort in algorithms:
            sort_name = sort.__name__

            # PROTECCIÓN CONTRA BOGO SORT
            if "bogo" in sort_name and n > 10:
                continue

            # Hacemos una copia para que el ordenamiento sea justo
            # y no afecte a los siguientes algoritmos
            data_copy = original_data.copy()

            # Medición precisa
            # Asumimos que la función ordena in-place o retorna
            start_time = time.perf_counter()
            sort(data_copy)
            end_time = time.perf_counter()

            elapsed = end_time - start_time

            results.append({
                "method": sort_name,
                "n": n,
                "time": elapsed
            })

    return results