# Descifrar el mensaje oculto por cifrado César que se encuentra en el archivo adjunto,
# descifrando por fuerza bruta. El alfabeto es este: "abcdefghijklmnñopqrstuvwxyz ,."

def cifrar_cesar(texto: str, alfabeto: str, desplazamiento: int) -> str:
    """
    Cifra una cadena usando el cifrado César con un desplazamiento fijo.

    Parámetros:
        texto (str): Texto que se desea cifrar.
        alfabeto (str): Cadena que representa el alfabeto permitido.
                        El orden del alfabeto define la permutación.
        desplazamiento (int): Número de posiciones que se desplazará cada carácter. 
                              Puede ser mayor que la longitud del alfabeto (se aplica módulo).

    Retorna:
        str: Texto cifrado. Los caracteres que no estén en el alfabeto se conservan sin cambio.
             Si un carácter original es mayúscula y su versión minúscula está en el alfabeto,
             el carácter cifrado conservará la mayúscula.
    """
    if not alfabeto: raise ValueError("El alfabeto no puede ser vacío.")
    
    longitud_alfabeto = len(alfabeto)
    desplazamiento = desplazamiento % longitud_alfabeto
    posiciones_caracteres = {caracter: indice for indice, caracter in enumerate(alfabeto)}

    texto_cifrado = []
    for caracter in texto:
        es_mayuscula = caracter.isupper()
        caracter_minuscula = caracter.lower()

        if caracter_minuscula in posiciones_caracteres:
            nueva_posicion = (posiciones_caracteres[caracter_minuscula] + desplazamiento) % longitud_alfabeto
            nuevo_caracter = alfabeto[nueva_posicion]
            if es_mayuscula: 
                nuevo_caracter = nuevo_caracter.upper()
            texto_cifrado.append(nuevo_caracter)
        else:
            texto_cifrado.append(caracter)

    return "".join(texto_cifrado)


def descifrar_cesar_fuerza_bruta(texto_cifrado: str, alfabeto: str):
    """
    Descifra un texto cifrado con el método César por fuerza bruta,
    respetando mayúsculas y minúsculas.

    Parámetros:
        texto_cifrado (str): Texto cifrado.
        alfabeto (str): Cadena que representa el alfabeto a usar,
                        por ejemplo "abcdefghijklmnñopqrstuvwxyz ,."

    Retorna:
        list[tuple[int, str]]: Lista de tuplas (desplazamiento, texto_descifrado)
    """
    resultados = []
    longitud_alfabeto = len(alfabeto)
    posiciones_caracteres = {caracter: indice for indice, caracter in enumerate(alfabeto)}
    
    for desplazamiento in range(longitud_alfabeto):
        texto_descifrado = ""
        for caracter in texto_cifrado:
            # Convertimos temporalmente a minúscula para buscar en el alfabeto
            c = caracter.lower()
            if c in posiciones_caracteres:
                # Calculamos la posición original
                nueva_posicion = (posiciones_caracteres[c] - desplazamiento) % longitud_alfabeto
                nuevo_caracter = alfabeto[nueva_posicion]
                # Conservamos mayúscula si el original era mayúscula
                if caracter.isupper():
                    nuevo_caracter = nuevo_caracter.upper()
                texto_descifrado += nuevo_caracter
            else:
                # Caracteres que no están en el alfabeto se conservan
                texto_descifrado += caracter
        resultados.append((desplazamiento, texto_descifrado))
    
    return resultados



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
    if n < 2: return None

    max_producto = float("-inf")
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
