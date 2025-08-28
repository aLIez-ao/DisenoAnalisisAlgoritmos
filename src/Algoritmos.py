# Dado un arreglo de n de números enteros y un entero k.
# Determinar si en el arreglo existe un par que dé como suma k.
# A[x]+A[x']=k


def existe_par_suma_k(arreglo, k):
    n = len(arreglo)
    for i in range(n):
        for j in range(i + 1, n):
            if arreglo[i] + arreglo[j] == k:
                return True
    print(f"El par es: {arreglo[i]}, {arreglo[j]}")
    return False


def existe_par_suma_k_optimizado(arreglo, k):
    diccionario = {}
    for numero in arreglo:
        complemento = k - numero
        if complemento in diccionario:
            return True
        diccionario[numero] = True
        print(diccionario)
    return False
