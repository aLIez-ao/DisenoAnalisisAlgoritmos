# -------------------------------
# Algoritmos de recursividad
# -------------------------------

# Crear una lista de enteros en Python y realizar la suma con recursividad
def suma_recursiva(lista):
    """Devuelve la suma de todos los elementos de una lista usando recursión."""
    if not lista: return 0
    return lista[0] + suma_recursiva(lista[1:])


# Contar los digitos de un entero positivo
def contar_digitos(n):
    """Devuelve el número de dígitos de un número entero positivo usando recursión."""
    if n < 10: return 1
    return 1 + contar_digitos(n // 10)


# Eliminar de un ADT pila el valor en la posición media.
def eliminar_medio(pila, n = None, pos = 0):
    """Elimina el elemento del medio de una pila representada como lista."""
    if n is None: n = len(pila)
    if pos == n // 2:
        pila.pop()
        return
    elemento = pila.pop()
    eliminar_medio(pila, n, pos + 1)
    pila.append(elemento)


# Verificar si una cadena es Palíndromo con recursividad
def es_palindromo(cadena):
    """Devuelve True si la cadena es un palíndromo, False en caso contrario."""
    cadena = cadena.replace(" ", "").lower()
    if len(cadena) <= 1: return True
    if cadena[0] != cadena[-1]: return False
    return es_palindromo(cadena[1:-1])


# Sucecsión de Fibonacci con recursividad
def fibonacci(n):
    """Devuelve el n-ésimo número de Fibonacci usando recursión."""
    if n <= 0:return "El número debe ser positivo"
    elif n == 1:return 0
    elif n == 2: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)


