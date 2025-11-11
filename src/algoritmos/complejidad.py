"""
El módulo contiene varias funciones para el análisis de la complejidad algorítmica, incluyendo ejemplos de bucles simples, bucles anidados, y operaciones sobre listas. Cada función está acompañada de comentarios detallados sobre su complejidad temporal T(n) y su notación Big O.
Funciones incluidas:
Cada función incluye un análisis detallado de su complejidad temporal, útil para fines educativos en el estudio de diseño y análisis de algoritmos.
"""

# Función 1: Suma de números naturales hasta 'tope'
def suma_naturales(tope):
    suma = 0                     # T(n) = 1
    for num in range(tope + 1):  # T(n) = tope + 1
        suma += num              # T(n) = 1 por iteración → total T(n) = tope + 1
    return suma                  # T(n) = 1
                                 # Complejidad total: T(n) = 1 + (tope + 1) + (tope + 1) + 1 = 
                                                    # T(n) = 2*(tope + 1) + 2 ≈ 
                                                    # T(n) ≈ 2*tope + 4


# ____________________________________________________________________________
# Función 2: Tres bucles anidados sobre la misma lista
def ejercicio3(lista):
    conteo = 0                           # T(n) = 1
    for numero1 in lista:                # T(n) = n
        for numero2 in lista:            # T(n) = n
            for numero3 in lista:        # T(n) = n
                print(numero1, numero3)  # T(n) = 1 por iteración → total T(n) = n^3
                conteo += 1              # T(n) = 1 por iteración → total T(n) = n^3
    return conteo                        # T(n) = 1
                                         # Complejidad total: T(n) = 1 + n*n*n*2 + 1 = 
                                                            # T(n) = 2*n^3 + 2


# ____________________________________________________________________________
# Función 3: Suma de lista + bucle anidado
def ejercicio4(lista):
    conteo = 0                    # T(n) = 1
    sume = 0                      # T(n) = 1
    for num in lista:             # T(n) = n
        sume += num               # T(n) = 1 por iteración → total T(n) = n
    print(f"La suma es: {sume}")  # T(n) = 1

    for i in lista:               # T(n) = n
        for j in lista:           # T(n) = n
            print(i, j)           # T(n) = 1 por iteración → total T(n) = n*n
            conteo += 1           # T(n) = 1 por iteración → total T(n) = n*n
    return conteo                 # T(n) = 1
                                  # Complejidad total: T(n) = 1+1+n+n+1 + n*n*2 + 1 = 
                                                     # T(n) = 2 + 2*n + 2*n^2 + 1 = 
                                                     # T(n) = 2*n^2 + 2*n + 3


# ____________________________________________________________________________
# Función 4: Bucle anidado entre dos listas diferentes
def ejercicio4_1(lista, lista2):
    conteo = 0                # T(n) = 1
    for i in lista:           # T(n) = n
        for j in lista2:      # T(n) = m
            print(i, j)       # T(n) = 1 por iteración → total T(n) = n*m
            conteo += 1       # T(n) = 1 por iteración → total T(n) = n*m
    return conteo             # T(n) = 1
                              # Complejidad total: T(n) = 1 + n*m*2 + 1 = 
                                                 # T(n) = 2*n*m + 2
                                                 

# Tarea: Analisis de algoritmos. Deteminar el T(n) de las siguientes funciones
# ____________________________________________________________________________

def tarea_uno(n):
    s = 0                               # T(n) = 1
    for i in range(n):                  # T(n) = n
        basura = i                      # T(n) = 1 por iteración -> total T(n) = n
        s += 1                          # T(n) = 1 por iteración -> total T(n) = n
        i = i                           # T(n) = 1 por iteración -> total T(n) = n
    return s                            # T(n) = 1
                                        # Complejidad total: T(n) = 1 + n + n + n + n + 1
                                        # T(n) = 4n + 2
                                        # El término dominante es n, por lo tanto, la complejidad es lineal.
                                        # Resultado final: O(n)

# ____________________________________________________________________________

def tarea_dos(n):
    cnt = 0                             # T(n) = 1
    for _ in range(n):                  # T(n) = n
        j = n                           # T(n) = 1 por iteración -> total T(n) = n
        j = j                           # T(n) = 1 por iteración -> total T(n) = n
        while j > 1:                    # T(n) = log2(n) por iteración -> total T(n) = n * log2(n)
            j //= 2                     # T(n) = 1 por iteración del while -> total T(n) = n * log2(n)
            cnt += 1                    # T(n) = 1 por iteración del while -> total T(n) = n * log2(n)
            cnt = cnt                   # T(n) = 1 por iteración del while -> total T(n) = n * log2(n)
    print("Fin del for")                # T(n) = 1
    return cnt                          # T(n) = 1
                                        # Complejidad total: T(n) = 1 + n + n + n + n * log2(n) + n * log2(n) + n * log2(n) + 1 + 1
                                        # T(n) = 3n + 3n * log2(n) + 3
                                        # El término dominante es n * log2(n), por lo tanto, la complejidad es log-lineal.
                                        # Resultado final: O(n log n)

# ____________________________________________________________________________

def tarea_tres(a):
    cnt = 0                             # T(n) = 1
    n = len(a)                          # T(n) = 1
    for i in range(n):                  # T(n) = n
        for j in range(i + 1, n):       # T(n) = (n * (n + 1) / 2) - n = n*(n-1)/2
            cnt += 1                    # T(n) = 1 por iteración del for interno -> total T(n) = n*(n-1)/2
            cnt = cnt                   # T(n) = 1 por iteración del for interno -> total T(n) = n*(n-1)/2
    return cnt                          # T(n) = 1
                                        # Complejidad total: T(n) = 1 + 1 + n + n*(n-1)/2 + n*(n-1)/2 + 1
                                        # T(n) = 2 + n + n*(n-1)
                                        # T(n) = 2 + n + n^2 - n
                                        # T(n) = n^2 + 2
                                        # El término dominante es n^2, por lo tanto, la complejidad es cuadrática.
                                        # Resultado final: O(n^2)

# ____________________________________________________________________________

def tarea_cuatro(a):
    n = len(a)                          # T(n) = 1
    total = 0                           # T(n) = 1
    n = (n * 2) // 2                     # T(n) = 1
    for i in range(n):                  # T(n) = n
        basura = 1                      # T(n) = 1 por iteración -> total T(n) = n
        nada = 0                        # T(n) = 1 por iteración -> total T(n) = n
        i = i                           # T(n) = 1 por iteración -> total T(n) = n
        for j in range(n):              # T(n) = n por iteración -> total T(n) = n * n = n^2
            total = total               # T(n) = 1 por iteración del for interno -> total T(n) = n^2
            k = k                       # T(n) = 1 por iteración del for interno -> total T(n) = n^2
            j = j                       # T(n) = 1 por iteración del for interno -> total T(n) = n^2
            total += a[i] + a[j] + a[k] # T(n) = 1 por iteración del for interno -> total T(n) = n^2
    return total                        # T(n) = 1
                                        # Complejidad total: T(n) = 1 + 1 + 1 + n + n + n + n + n^2 + n^2 + n^2 + n^2 + n^2 + 1
                                        # T(n) = 5n^2 + 4n + 4
                                        # El término dominante es n^2, por lo tanto, la complejidad es cuadrática.
                                        # Resultado final: O(n^2)

# ____________________________________________________________________________

def tarea_operation(numbers):
    result = []                         # T(n) = 1
    for number in numbers:              # T(n) = N
        count = 0                       # T(n) = 1 por iteración -> total T(n) = N
        while number >= 1:              # T(n) = log2(number) por iteración
            number //= 2                # T(n) = 1 por iteración del while
            count += 1                  # T(n) = 1 por iteración del while
        result.append(count)            # T(n) = 1 por iteración -> total T(n) = N
    return result                       # T(n) = 1
                                        # Complejidad total: T(n) = 1 + N + N + sum(log(number) for number in numbers) + N + 1
                                        # Si m es el valor máximo en la lista, el peor caso del bucle while es log(m).
                                        # T(n) ≈ N * log(m)
                                        # La complejidad depende del número de elementos (N) y el valor de estos (m).
                                        # Resultado final: O(N log m)

                                                 
