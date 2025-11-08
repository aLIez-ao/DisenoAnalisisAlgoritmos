from typing import List, Tuple, Optional, Set, Dict, Any, Union
from lib import leer_archivo


# ============================================================================
# FUNCIONES DE LECTURA Y PARSEO
# ============================================================================


def parsear_laberinto(lineas: List[str]) -> Dict[str, Any]:
    """Convierte las líneas del archivo en una estructura de laberinto."""
    if len(lineas) < 2: return {}

    filas = int(lineas[0].strip())
    columnas = int(lineas[1].strip())

    def parsear_celda(celda: str) -> Union[str, int]:
        """Convierte el texto de la celda en entero o símbolo especial."""
        return celda if celda in {'E', 'S'} else int(celda)

    tablero: List[List[Union[str, int]]] = [
        list(map(parsear_celda, lineas[i + 2].strip().split()))
        for i in range(filas)
    ]

    posiciones = [(i, j) for i in range(filas) for j in range(columnas)]

    entrada = next((pos for pos in posiciones if obtener_celda(tablero, pos) == 'E'), None)
    salida = next((pos for pos in posiciones if obtener_celda(tablero, pos) == 'S'), None)

    return {
        'tablero': tablero,
        'filas': filas,
        'columnas': columnas,
        'entrada': entrada,
        'salida': salida,
    }


def obtener_celda(tablero: List[List[Union[str, int]]], pos: Tuple[int, int]) -> Union[str, int, None]:
    """Devuelve el valor de una celda dada su posición (fila, columna)."""
    fila, col = pos
    if 0 <= fila < len(tablero) and 0 <= col < len(tablero[0]): return tablero[fila][col]
    return None



# ============================================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================================

def es_posicion_valida(tablero: List[List], pos: Tuple[int, int], visitados: Set[Tuple[int, int]]) -> bool:
    """Verifica si una posición es válida para moverse"""
    fila, col = pos
    filas, columnas = len(tablero), len(tablero[0])
    
    # Verificar límites, si es pared o si ya fue visitado
    if not (0 <= fila < filas and 0 <= col < columnas): return False
    if tablero[fila][col] == 1: return False
    if pos in visitados: return False
    
    return True


def obtener_vecinos_validos(tablero: List[List], pos: Tuple[int, int], 
                            visitados: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Obtiene todas las posiciones vecinas válidas"""
    fila, col = pos
    # arriba, derecha, abajo, izquierda
    movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    vecinos = [(fila + df, col + dc) for df, dc in movimientos]
    
    return list(filter(lambda v: es_posicion_valida(tablero, v, visitados), vecinos))


# ============================================================================
# FUNCIONES DE BACKTRACKING
# ============================================================================

def backtracking(tablero: List[List], pos_actual: Tuple[int, int], 
                salida: Tuple[int, int], visitados: Set[Tuple[int, int]], 
                pila: List[Tuple[int, int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Resuelve el laberinto usando backtracking recursivo (programación funcional)
    Retorna la pila con la ruta si encuentra solución, None en caso contrario
    """
    # Crear nueva pila y conjunto de visitados (inmutabilidad)
    nueva_pila = pila + [pos_actual]
    nuevos_visitados = visitados | {pos_actual}
    
    # Caso base: llegamos a la salida
    if pos_actual == salida: return nueva_pila
    
    # Obtener vecinos válidos
    vecinos = obtener_vecinos_validos(tablero, pos_actual, nuevos_visitados)
    
    # Intentar cada vecino usando recursión
    def explorar_vecinos(vecinos_restantes):
        if not vecinos_restantes: return None
        
        vecino = vecinos_restantes[0]
        resultado = backtracking(tablero, vecino, salida, nuevos_visitados, nueva_pila)
        
        if resultado is not None: return resultado
        
        return explorar_vecinos(vecinos_restantes[1:])
    
    return explorar_vecinos(vecinos)


def resolver_laberinto_func(laberinto: dict) -> Optional[List[Tuple[int, int]]]:
    """Resuelve el laberinto y retorna la ruta de solución"""
    if not laberinto or not laberinto.get('entrada') or not laberinto.get('salida'):
        return None
    
    return backtracking(
        laberinto['tablero'],
        laberinto['entrada'],
        laberinto['salida'],
        set(),
        []
    )


# ============================================================================
# FUNCIONES DE VISUALIZACIÓN (efectos secundarios controlados)
# ============================================================================

def imprimir_tablero(tablero: List[List], titulo: str = "Tablero:") -> None:
    """Imprime el tablero"""
    print(f"\n{titulo}")
    
    for fila in tablero:
        print(' '.join(str(celda) for celda in fila))
    
    print()


def crear_tablero_con_ruta(tablero: List[List], ruta: List[Tuple[int, int]]) -> List[List]:
    """Crea una copia del tablero marcando la ruta con asteriscos"""
    # Crear copia profunda
    tablero_copia = [fila[:] for fila in tablero]
    
    # Marcar la ruta
    for fila, col in ruta:
        if tablero_copia[fila][col] not in ['E', 'S']:
            tablero_copia[fila][col] = '*'
    
    return tablero_copia


def imprimir_ruta(ruta: List[Tuple[int, int]]) -> None:
    """Imprime la ruta de solución paso a paso"""
    print("\n" + "=" * 50)
    print("RUTA DE SOLUCIÓN:")
    print("=" * 50)
    print(f"\nTotal de pasos: {len(ruta)}\n")
    
    for i, (fila, col) in enumerate(ruta):
        print(f"Paso {i + 1}: ({fila}, {col})")
    
    print("\n" + "=" * 50)


def imprimir_resultado(laberinto: dict, ruta: Optional[List[Tuple[int, int]]]) -> None:
    """Imprime el resultado de la resolución del laberinto"""
    print(f"\nLaberinto: {laberinto['filas']}x{laberinto['columnas']}")
    print(f"Entrada: {laberinto['entrada']}")
    print(f"Salida: {laberinto['salida']}")
    
    imprimir_tablero(laberinto['tablero'], "Laberinto original:")
    
    if ruta:
        print("\n¡Solución encontrada!")
        imprimir_ruta(ruta)
        
        tablero_con_ruta = crear_tablero_con_ruta(laberinto['tablero'], ruta)
        imprimir_tablero(tablero_con_ruta, "Laberinto con la ruta marcada (*):")
    else:
        print("\nNo existe solución para este laberinto")


# ============================================================================
# FUNCIÓN PRINCIPAL (COMPOSICIÓN DE FUNCIONES)
# ============================================================================

def resolver_laberinto(archivo: str) -> bool:
    """
    Función principal para resolver un laberinto desde un archivo
    Usa composición de funciones puras
    
    Args:
        archivo: ruta del archivo .txt con el laberinto
    
    Returns:
        True si encuentra solución, False en caso contrario
    """
    # Pipeline funcional: leer -> parsear -> resolver -> imprimir
    lineas = leer_archivo(archivo)
    
    if not lineas: return False
    
    laberinto = parsear_laberinto(lineas)
    
    if not laberinto:
        print("Error: No se pudo parsear el laberinto")
        return False
    
    ruta = resolver_laberinto_func(laberinto)
    imprimir_resultado(laberinto, ruta)
    
    return ruta is not None
