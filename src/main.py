import random
from lib.ejecutar_funcion import *
from lib import lector_txt


if __name__ == "__main__":

    n = random.randint(1, 100)
    arreglo = generar_arreglo(20)
    lista = generar_lista(n)
    pila = generar_pila(n)
    texto = "anita lava la tina"
    ruta = lector_txt.leer_txt(r"resources\texto.txt")
    # ruta = r"resources\hola_mundo.txt"

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
        "es_palindromo": lambda: ejecutar_es_palindromo(texto),
        
        # Algoritmos de fuerza bruta
        "maximo_producto": lambda: ejecutar_maximo_producto(arreglo),
        "cifrar_cesar": lambda: ejecutar_cifrar_cesar(ruta, n, ESP),
        "descifrar_cesar": lambda: ejecutar_descifrar_cesar(ruta, ESP),
        "ejecutar_cifrar_cesar_texto": lambda: ejecutar_cifrar_decifrar_cesar(ruta, 3, ESP),

    }


    # -------------------------------
    # Ejecutar algoritmo elegido
    # -------------------------------
    algoritmo_ejecutar = "descifrar_cesar"
    funciones[algoritmo_ejecutar]()
