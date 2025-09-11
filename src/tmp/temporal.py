numero = [1, 2, 3]


## Ejemplo 4.1
## El analsis es de T(n) = 4+n+2n^2
## El analisis de S(n)º  es de S(n) = 5+n
def unaFuncionCualquiera(lista):
    conteo = 0
    suma = 0
    for num in lista:
        suma += num
    print("La sumatoria de los numeros en la lista es: ", suma)

    for numero1 in lista:
        for numero2 in lista:
            print(numero1, numero2)
            conteo += 1
    return conteo


## Ejemplo 4.2
## El analisis de T(n) = 1 + 2(n*m) + 1 = 2 + 2nm
## El analisis de S(n) = n + m + 1 + 2 = n + m + 3


# Ejemplo 5
## El analisis de T(n) = 1+n+2n^2
## El analisis de S(n) = 11
def otraFuncionCualquiera(n):
    a2d = Array2D(n, n)

    total = 0
    for i in range(n):
        sumaFila = 0
        for j in range(n):
            sumaFila += a2d.getItem(i, j)
        total += a2d.getItem(i, j)


## El analisis de T(n) = 1+2n+n^2
## El analisis de S(n) =
def otraFuncionCualquieraMejorarda(n):
    a2d = Array2D(n, n)

    total = 0
    for i in range(n):
        sumaFila = 0
        for j in range(n):
            sumaFila += a2d.getItem(i, j)
    total += a2d.getItem(i, j)


# Ejemplo
## El analisis de T(n) =
## El analisis de S(n) =

## Nata:
## tipos de for:
## for i in range(n):
##   for i in range(n):  # O(n)

## for i in range(n):
##   4 lineas de codigo -> 4n
##   for i in range(n):
##      2 lineas de codigo -> 2n^2


# funcion de factorial (Recursividad)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Funcion cuenta regresiva (Recursividad)
def cuentaRegresiva(n):
    if n == 0:
        print("Despegue!")
    else:
        print(n)
        cuentaRegresiva(n - 1)


def cuentaRegresivaMejorada(n):  # variar la posicion de la llamada recursiva

    print(n)
    if n > 0:
        cuentaRegresivaMejorada(n - 1)


# Funcion de la serie de Fibonacci (Recursividad)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
