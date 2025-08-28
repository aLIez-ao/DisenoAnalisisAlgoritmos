import random
import Algoritmos

if __name__ == "__main__":
    arreglo = []
    k = random.randint(0, 100)

    for i in range(100):
        arreglo.append(i)

    existe = Algoritmos.existe_par_suma_k(arreglo, k)
    print(f"Existe un par que suma {k}: {existe}")

    existe_optimizado = Algoritmos.existe_par_suma_k_optimizado(arreglo, k)
    print(f"Existe un par que suma {k} (optimizado): {existe_optimizado}")
