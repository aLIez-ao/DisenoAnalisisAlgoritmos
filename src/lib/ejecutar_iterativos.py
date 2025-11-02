from colorama import Fore, Style
from algoritmos import *

def ejecutar_suma_digitos_iterativo(numeros):
    """
    Ejecuta la suma de dígitos de uno o varios números usando
    suma_digitos_iterativo y muestra resultados de forma visual.
    
    Args:
        numeros: int o lista de ints
    """
    if isinstance(numeros, int):
        numeros = [numeros]

    for n in numeros:
        print("=" * 50)
        print(f"{Fore.CYAN}Procesando número: {n}{Style.RESET_ALL}")
        suma_total = suma_digitos_iterativo(n)
        print(f"{Fore.YELLOW}Suma de los dígitos de {n}: {Fore.GREEN}{suma_total}{Style.RESET_ALL}")
        print("=" * 50, "\n")


def ejecutar_mcd_iterativo(a, b):
    """
    Ejecuta el cálculo del MCD de dos números usando mcd_iterativo
    y muestra el resultado de forma visual en consola.
    
    Args:
        a: Primer número
        b: Segundo número
    """
    print("=" * 50)
    print(f"{Fore.CYAN}Calculando MCD de {a} y {b}{Style.RESET_ALL}")
    resultado = mcd_iterativo(a, b)
    print(f"{Fore.YELLOW}El MCD de {a} y {b} es: {Fore.GREEN}{resultado}{Style.RESET_ALL}")
    print("=" * 50, "\n")