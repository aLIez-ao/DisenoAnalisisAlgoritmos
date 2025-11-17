import matplotlib.pyplot as plt

def visualizar_puntos(puntos: list, rangos: list | None = None):
    """
    Dibuja los puntos en un plano cartesiano.
    
    Args:
        puntos: La lista de tuplas (x, y).
        rangos: (Opcional) La lista de resultados con rangos para colorear/etiquetar.
    """
    x_coords = [p[0] for p in puntos]
    y_coords = [p[1] for p in puntos]

    plt.figure(figsize=(8, 6))
    
    # Dibujar puntos
    plt.scatter(x_coords, y_coords, color='blue', marker='o')
    
    # Etiquetar cada punto con su coordenada (y su rango si existe)
    for i, (x, y) in enumerate(puntos):
        texto = f"P{i}"
        if rangos:
            # Si pasamos los resultados, mostramos el rango calculado
            # rangos debe ser la lista [x, y, id, rango]
            rango_val = rangos[i][3] # Asumiendo que rangos está ordenado por ID
            texto += f"\nR:{rango_val}"
            
        plt.text(x + 0.5, y + 0.5, texto, fontsize=9)

    plt.title("Visualización de Dominancia en R2")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()