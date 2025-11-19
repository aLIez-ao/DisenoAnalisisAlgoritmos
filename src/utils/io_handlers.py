from typing import List, NamedTuple, Tuple

class Point(NamedTuple):
    x: int
    y: int

def read_campo_file(filepath: str) -> List[Point]:
    """
    Lee el archivo campo.in.
    Termina la lectura al encontrar -1 -1.
    """
    points = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                parts = list(map(int, line.strip().split()))
                if len(parts) != 2:
                    continue
                
                x, y = parts
                if x == -1 and y == -1:
                    break
                
                points.append(Point(x, y))
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no existe.")
        return []
    
    return points

def write_campo_file(filepath: str, points: Tuple[Point, Point, Point]) -> None:
    """Escribe los 3 puntos resultantes en campo.out."""
    with open(filepath, 'w') as f:
        for p in points:
            f.write(f"{p.x} {p.y}\n")