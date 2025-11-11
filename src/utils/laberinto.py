def leer_dimensiones(f) -> tuple[int, int] | None:
    """Lee y valida las dimensiones del laberinto desde el archivo."""
    try:
        filas = int(f.readline().strip())
        columnas = int(f.readline().strip())
        return filas, columnas
    except ValueError:
        print("Error: Las primeras dos líneas deben ser números enteros.")
        return None


def procesar_linea(linea: str, columnas: int, r: int) -> list[str] | None:
    """Procesa una línea del laberinto y valida número de columnas."""
    fila = linea.strip().split(',')
    if len(fila) != columnas:
        print(f"Error: La fila {r} tiene {len(fila)} columnas, se esperaban {columnas}.")
        return None
    return fila


def buscar_entradas_y_salidas(laberinto: list[list[str]]) -> tuple | None:
    """Busca las posiciones de 'E' y 'S' en la matriz."""
    entrada = salida = None
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if celda == 'E': entrada = (i, j)
            elif celda == 'S': salida = (i, j)
    if not entrada:
        print("Error: No se encontró la 'E' (Entrada).")
        return None
    if not salida:
        print("Error: No se encontró la 'S' (Salida).")
        return None
    return entrada, salida


def cargar_laberinto(ruta_archivo: str) -> tuple | None:
    """
    Carga un laberinto desde un archivo .txt siguiendo el formato:
    - 1ª línea: número de filas
    - 2ª línea: número de columnas
    - Resto: matriz separada por comas, con 'E' y 'S'
    """
    try:
        with open(ruta_archivo, 'r') as f:
            dimensiones = leer_dimensiones(f)
            
            if not dimensiones: return None
            filas, columnas = dimensiones

            laberinto = []
            for i, linea in enumerate(f):
                if not linea.strip(): continue
                fila = procesar_linea(linea, columnas, i)
                
                if fila is None: return None
                laberinto.append(fila)

            if len(laberinto) != filas:
                print(f"Error: Se esperaban {filas} filas, se leyeron {len(laberinto)}.")
                return None
            resultado = buscar_entradas_y_salidas(laberinto)
            
            if not resultado: return None
            entrada, salida = resultado
            
            return laberinto, entrada, salida

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    return None
