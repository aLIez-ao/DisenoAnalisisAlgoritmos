import random
from colorama import Fore, Style, init
from algoritmos import *

# Inicializar colorama para Windows
init(autoreset=True)

if __name__ == "__main__":
    # Generamos un arreglo ordenado de tamaño n
    arreglo = list(range(100))

    # Elegimos dos índices aleatorios distintos para garantizar que el par exista
    i, j = random.sample(range(len(arreglo)), 2)
    k = arreglo[i] + arreglo[j]

    print(Style.BRIGHT + f"\n{'='*40}")
    print(Style.BRIGHT + f" Buscando si existe un par que sume {k} ")
    print(f"{'='*40}\n")

    # Ejecutar algoritmos
    existe = existe_par_suma_k(arreglo, k)
    existe_optimizado = existe_par_suma_k_optimizado(arreglo, k)

    # Resultado final
    print(Style.BRIGHT + "\n" + "=" * 40)
    if existe or existe_optimizado:
        print(Fore.GREEN + Style.BRIGHT + f"✅ Existe al menos un par que suma {k}.")
    else:
        print(Fore.RED + Style.BRIGHT + f"❌ No existe ningún par que sume {k}.")
    print("=" * 40 + "\n")
