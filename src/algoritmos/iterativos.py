# Suma de dígitos de un número natural

def suma_digitos_iterativo(n):
    """
    Calcula la suma de los dígitos de n de forma iterativa.
    
    Args:
        n: Número natural (entero positivo)
    
    Returns:
        Suma de los dígitos de n
    """
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma



# Máximo Común Divisor (MCD) - Algoritmo de Euclides

def mcd_iterativo(a, b):
    """
    Calcula el MCD de dos números usando el algoritmo de Euclides iterativo.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        Máximo Común Divisor de a y b
    """
    while b != 0:
        residuo = a % b
        a = b
        b = residuo
    return a

