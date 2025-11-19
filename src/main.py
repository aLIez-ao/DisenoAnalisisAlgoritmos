from runner import *

def main():
    # ================ Generar datos de prueba =========================
    test_sizes = [10, 100, 1000, 10000, 100000]


    # ================= Diccionario de funciones =======================
    function = {
        "benchmark": lambda: run_benchmark(test_sizes),
        "triangulo": lambda: run_triangle_challenge(),
    }

    # ================= Ejecutar algoritmo elegido =====================
    execute = "triangulo"
    function[execute]()

if __name__ == "__main__":
    main()