from colorama import Fore, Style, init
from algoritmos.dinamicos import resolver_laberinto
from utils.laberinto import cargar_laberinto

# Inicializar colorama (necesario para Windows)
init(autoreset=True)

def imprimir_laberinto_visual(laberinto: list, ruta: set | None = None):
    """
    Imprime el laberinto con colores.
    - '█' (Pared)
    - 'E' (Entrada)
    - 'S' (Salida)
    - '·' (Ruta de solución)
    - ' ' (Camino vacío)
    """
    if ruta is None:
        ruta = set()
    
    # Imprimir borde superior
    print(Fore.WHITE + " " + "█" * (len(laberinto[0]) * 2 + 1))

    for r, fila in enumerate(laberinto):
        print(Fore.WHITE + " █", end=" ") # Borde izquierdo
        for c, celda in enumerate(fila):
            pos = (r, c)
            
            if celda == 'E':
                print(Fore.YELLOW + Style.BRIGHT + 'E', end=" ")
            elif celda == 'S':
                print(Fore.MAGENTA + Style.BRIGHT + 'S', end=" ")
            elif pos in ruta:
                print(Fore.GREEN + Style.BRIGHT + '·', end=" ") # Marcador de ruta
            elif celda == '1':
                print(Fore.WHITE + '█', end=" ") # Pared
            elif celda == '0':
                print(' ', end=" ") # Camino
        print(Fore.WHITE + "█") # Borde derecho

    # Imprimir borde inferior
    print(Fore.WHITE + " " + "█" * (len(laberinto[0]) * 2 + 1))

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
    print(Fore.CYAN + f"Entrada: {entrada} | Salida: {salida}\n" + Style.RESET_ALL)

    # --- 1. Mostrar Laberinto Original ---
    print(Fore.YELLOW + "--- 1. Laberinto Original ---" + Style.RESET_ALL)
    imprimir_laberinto_visual(laberinto)
    
    # --- Resolver ---
    ruta_solucion_lista = resolver_laberinto(laberinto, entrada, salida)

    if ruta_solucion_lista:
        # Convertir lista a set para búsqueda rápida en la impresión
        ruta_solucion_set = set(ruta_solucion_lista)
        
        # --- 2. Mostrar Laberinto Resuelto ---
        print(Fore.GREEN + "\n--- 2. Laberinto Resuelto (· = ruta) ---" + Style.RESET_ALL)
        imprimir_laberinto_visual(laberinto, ruta_solucion_set)

       # --- 3. Mostrar Decisiones (Ruta) ---
        print(Fore.GREEN + "\n--- 3. Decisiones Tomadas (Ruta) ---" + Style.RESET_ALL)
        
        # Constante para definir cuántos pasos mostrar por línea
        PASOS_POR_LINEA = 15
        
        # Iterar sobre la lista de la solución en "trozos" de 15
        for i in range(0, len(ruta_solucion_lista), PASOS_POR_LINEA):
            
            # Obtener el subconjunto (chunk) de pasos para esta línea
            # p.ej., [0:15], luego [15:30], etc.
            chunk = ruta_solucion_lista[i : i + PASOS_POR_LINEA]
            
            # Convertir cada tupla (paso) a un string con color
            pasos_con_color = [f"{Fore.CYAN}{paso}{Style.RESET_ALL}" for paso in chunk]
            
            # Unir los pasos de esta línea con una flecha blanca
            linea_de_pasos = f" {Fore.WHITE}→{Style.RESET_ALL} ".join(pasos_con_color)
            
            # Imprimir la línea completa
            print(f"  {linea_de_pasos}")

        
        print(Fore.MAGENTA + f"\n🔚 Longitud de la ruta: {len(ruta_solucion_lista)} pasos\n" + Style.RESET_ALL)
    
    else:
        print(Fore.RED + "\n🚫 No se encontró ninguna solución para el laberinto.\n" + Style.RESET_ALL)