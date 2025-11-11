def movimiento_valido(laberinto: list, fila: int, columna: int, visitados: set) -> bool:
    """Verifica si una celda es válida para moverse (dentro de límites, no pared, no visitada)."""
    f_total = len(laberinto)
    c_total = len(laberinto[0])
    
    if not (0 <= fila < f_total and 0 <= columna < c_total): return False
    if laberinto[fila][columna] == '1': return False
    if (fila, columna) in visitados: return False
    
    return True


def vecinos(fila: int, columna: int) -> list[tuple[int, int]]:
    """Retorna las posiciones vecinas en orden: Abajo, Arriba, Derecha, Izquierda."""
    return [
        (fila + 1, columna),  # Abajo
        (fila - 1, columna),  # Arriba
        (fila, columna + 1),  # Derecha
        (fila, columna - 1)   # Izquierda
    ]


def backtrack(
    laberinto: list,
    actual: tuple[int, int],
    salida: tuple[int, int],
    visitados: set,
    stack: list
) -> bool:
    """Función recursiva que implementa el backtracking sobre el laberinto."""
    fila, columna = actual

    # Caso base: llegar a la salida
    if actual == salida:
        stack.append(actual)
        return True

    # Marcar actual como visitada
    visitados.add(actual)
    stack.append(actual)

    # Explorar vecinos válidos
    for nueva_fila, nueva_col in vecinos(fila, columna):
        if movimiento_valido(laberinto, nueva_fila, nueva_col, visitados):
            if backtrack(laberinto, (nueva_fila, nueva_col), salida, visitados, stack):
                return True

    # Retroceso: remover de la pila
    stack.pop()
    return False


def resolver_laberinto(laberinto: list, entrada: tuple, salida: tuple) -> list | None:
    """
    Resuelve el laberinto usando backtracking y una pila.
    Retorna la ruta (pila) si hay solución, o None si no existe.
    """
    pila_solucion = []
    visitados = set()

    if backtrack(laberinto, entrada, salida, visitados, pila_solucion):
        return pila_solucion
    return None