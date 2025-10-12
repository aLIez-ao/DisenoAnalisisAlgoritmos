# Descifrar el mensaje oculto por cifrado César que se encuentra en el archivo adjunto,
# descifrando por fuerza bruta. El alfabeto es este: "abcdefghijklmnñopqrstuvwxyz ,."


# Dado un arreglo de enteros encuentra dos números en el arreglo cuyo producto sea el más alto empleando fuerza bruta.
def encontrar_maximo_producto(arreglo):
    """
    Encuentra dos números en el arreglo cuyo producto sea el más alto.
    Método: fuerza bruta (compara todos los pares posibles).
    Complejidad temporal: O(n^2)

    Args:
        arreglo (list[int]): lista de números enteros.

    Returns:
        tuple[int, int, int]: (num1, num2, producto_máximo)
        o None si el arreglo tiene menos de dos elementos.
    """
    n = len(arreglo)
    if n < 2:
        return None

    max_producto = float('-inf')
    mejor_par = (None, None)

    # Comparar todos los pares posibles (fuerza bruta)
    for i in range(n - 1):
        for j in range(i + 1, n):
            producto = arreglo[i] * arreglo[j]

            # Si encontramos un producto mayor, actualizamos
            if producto > max_producto:
                max_producto = producto
                mejor_par = (arreglo[i], arreglo[j])

    return mejor_par[0], mejor_par[1], max_producto

