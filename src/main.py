import random
from lib import *



if __name__ == "__main__":

    n = random.randint(1, 100)
    arreglo = generar_arreglo(20)
    lista = generar_lista(n)
    pila = generar_pila(n)
    cadena = "anita lava la tina"
    texto = "Hola Mundo"
    
    ESP = "abcdefghijklmnñopqrstuvwxyz ,."
    ING = "abcdefghijklmnopqrstuvwxyz ,."



    # -------------------------------
    # Diccionario de funciones
    # -------------------------------
    funciones = {
        # Algoritmos optimizados
        "par_suma_k": lambda: ejecutar_par_suma_k(arreglo),
        "busqueda_lineal": lambda: ejecutar_busqueda_lineal(arreglo, random.choice(arreglo)),
        
        # Algoritmos recursivos
        "suma_recursiva": lambda: ejecutar_suma_recursiva(lista),
        "contar_digitos": lambda: ejecutar_contar_digitos(n),
        "eliminar_medio": lambda: ejecutar_eliminar_medio(pila),
        "es_palindromo": lambda: ejecutar_es_palindromo(cadena),
        
        # Algoritmos de fuerza bruta
        "maximo_producto": lambda: ejecutar_maximo_producto(arreglo),
        "cifrar_cesar": lambda: ejecutar_cifrar_cesar(texto, n, ESP),
        "descifrar_cesar": lambda: ejecutar_descifrar_cesar(texto, ESP),

    }


    # -------------------------------
    # Ejecutar algoritmo elegido
    # -------------------------------
    algoritmo_ejecutar = "cifrar_cesar"
    funciones[algoritmo_ejecutar]()
