from colorama import Fore, Style
from algoritmos import *
from utils import *

def run_resolver_laberinto(ruta_archivo: str):
    """
    Ejecuta el proceso completo de carga y resolución de un laberinto,
    mostrando la ruta encontrada (si existe) con colores.
    """
    print(Style.BRIGHT + f"\n🏁 Resolución del laberinto desde: {ruta_archivo}" + Style.RESET_ALL)

    datos = cargar_laberinto(ruta_archivo)
    if not datos:
        print(Fore.RED + "❌ No se pudo cargar el laberinto.\n" + Style.RESET_ALL)
        return

    laberinto, entrada, salida = datos
    print(Fore.YELLOW + f"Entrada: {entrada} | Salida: {salida}\n" + Style.RESET_ALL)

    ruta_solucion = resolver_laberinto(laberinto, entrada, salida)

    if ruta_solucion:
        print(Fore.GREEN + "✅ Ruta encontrada:\n" + Style.RESET_ALL)
        for paso in ruta_solucion:
            print(f"{Fore.CYAN} → {paso}{Style.RESET_ALL}")
        print(Fore.MAGENTA + f"\n🔚 Longitud de la ruta: {len(ruta_solucion)} pasos\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "🚫 No se encontró ninguna solución para el laberinto.\n" + Style.RESET_ALL)
