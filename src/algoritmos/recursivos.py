# Suma de dígitos de un número natural

def suma_digitos_recursivo(n):
    """
    Calcula la suma de los dígitos de n de forma recursiva.
    
    Args:
        n: Número natural (entero positivo)
    
    Returns:
        Suma de los dígitos de n
    """
    # Caso base: si n es menor que 10, es un solo dígito
    if n < 10: return n
    
    # Caso recursivo: último dígito + suma de los demás
    return (n % 10) + suma_digitos_recursivo(n // 10)


# Máximo Común Divisor (MCD) - Algoritmo de Euclides

def mcd_recursivo(a, b):
    """
    Calcula el MCD de dos números usando el algoritmo de Euclides recursivo.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        Máximo Común Divisor de a y b
    """
    # Caso base: si b es 0, el MCD es a
    if b == 0: return a
    
    # Caso recursivo: MCD(a, b) = MCD(b, a mod b)
    return mcd_recursivo(b, a % b)