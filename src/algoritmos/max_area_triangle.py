# src/algoritmos/max_area_triangle.py
import itertools
from typing import List, Tuple, Optional
from utils.io_handlers import Point

# ========================== UTILIDADES GEOMÉTRICAS ======================================

def _triangle_double_area(p1: Point, p2: Point, p3: Point) -> int:
    """
    Calcula el doble del área usando el producto cruz (determinante).
    Retornamos el doble para trabajar solo con enteros y evitar floats.
    Formula: |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
    """
    return abs(p1.x * (p2.y - p3.y) + 
               p2.x * (p3.y - p1.y) + 
               p3.x * (p1.y - p2.y))

def _monotone_chain(points: List[Point]) -> List[Point]:
    """
    Algoritmo Monotone Chain para encontrar el Convex Hull.
    Complejidad: O(n log n) debido al ordenamiento.
    """
    if len(points) <= 2: return points
    
    # Ordenar por x, luego por y
    sorted_points = sorted(points, key=lambda p: (p.x, p.y))

    # Construir mitad inferior
    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and _cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Construir mitad superior
    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and _cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenar (eliminando el último punto de cada lista porque se repite)
    return lower[:-1] + upper[:-1]

def _cross_product(o: Point, a: Point, b: Point) -> int:
    """Producto cruz de los vectores OA y OB. >0 izquierda, <0 derecha."""
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


# ====================== SOLUCIONES PÚBLICAS ==========================================

def solve_brute_force(points: List[Point]) -> Tuple[Point, Point, Point]:
    """
    Estrategia: Probar todas las combinaciones posibles de 3 puntos.
    Complejidad: O(n³) combinaciones.
    Para N=500, 500^3 = 125,000,000 (Aceptable pero lento).
    """
    max_area = -1.0
    best_triangle = (points[0], points[1], points[2])

    # itertools.combinations es la forma Pythonica de hacer 3 bucles anidados
    for p1, p2, p3 in itertools.combinations(points, 3):
        area = _triangle_double_area(p1, p2, p3)
        if area > max_area:
            max_area = area
            best_triangle = (p1, p2, p3)
    
    return best_triangle

def solve_optimized(points: List[Point]) -> Tuple[Point, Point, Point]:
    """
    Estrategia: Reducir el espacio de búsqueda al Convex Hull.
    
    Teorema: El triángulo de área máxima tiene sus vértices en el Convex Hull.
    
    Complejidad:
        1. Convex Hull: O(n log n)
        2. Búsqueda en Hull: O(h³) donde h es # puntos en el hull.
        
    En el caso promedio h << n, haciendo esto mucho más rápido.
    """
    if len(points) < 3:
        raise ValueError("Se necesitan al menos 3 puntos")

    # Filtrar puntos irrelevantes
    hull_points = _monotone_chain(points)

    # Si el hull tiene menos de 3 puntos (colineales), usar los originales
    # (aunque el área será 0, es un caso borde)
    target_points = hull_points if len(hull_points) >= 3 else points

    # Aplicar fuerza bruta solo sobre los supervivientes
    return solve_brute_force(target_points)