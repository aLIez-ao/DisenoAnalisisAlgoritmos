"""
visualizer.py — Módulo para la generación de gráficos.
Encapsula la lógica de Matplotlib para mantener el runner limpio.
"""

import matplotlib.pyplot as plt
from typing import List, Tuple, Optional
from .io_handlers import Point

def plot_triangle_solution(
    all_points: List[Point], 
    triangle: Tuple[Point, Point, Point],
    hull_points: Optional[List[Point]] = None
) -> None:
    """
    Genera una visualización del campo de postes y el triángulo solución.

    Args:
        all_points: Lista completa de todos los postes (se pintarán en gris).
        triangle: Los 3 puntos que forman el triángulo de área máxima (en rojo).
        hull_points: (Opcional) Puntos del cierre convexo para visualizar la optimización.
    """
    plt.figure(figsize=(10, 8))
    plt.title("Solución: Triángulo de Área Máxima")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True, linestyle='--', alpha=0.6)

    # 1. Desempaquetar coordenadas de todos los puntos (Estilo Pythonico con zip)
    # zip(*lista) transpone la lista de tuplas [(x1,y1), (x2,y2)] -> [(x1,x2), (y1,y2)]
    if all_points:
        xs, ys = zip(*all_points)
        plt.scatter(xs, ys, c='gray', alpha=0.5, s=20, label='Postes (N)')

    # 2. Pintar el Convex Hull (si se proporciona)
    if hull_points:
        # Necesitamos repetir el primer punto al final para cerrar el polígono visualmente
        hull_loop = hull_points + [hull_points[0]]
        hx, hy = zip(*hull_loop)
        plt.plot(hx, hy, 'g--', linewidth=1, alpha=0.7, label='Convex Hull (Perímetro)')
        plt.scatter(hx, hy, c='green', s=30, marker='x')

    # 3. Pintar el Triángulo Solución
    # También cerramos el ciclo añadiendo el primer punto al final
    tri_loop = list(triangle) + [triangle[0]]
    tx, ty = zip(*tri_loop)

    plt.plot(tx, ty, c='red', linewidth=2, label='Triángulo Máximo')
    plt.fill(tx, ty, c='red', alpha=0.2) # Relleno suave
    plt.scatter(tx, ty, c='red', s=100, zorder=5) # Vértices destacados

    plt.legend()
    
    # Ajustar márgenes
    plt.tight_layout()
    
    print("Mostrando gráfico...")
    plt.show()