
# Algoritmos y Geometría Computacional

> **Proyecto Final - Diseño y Análisis de Algoritmos**
>
> *Ingeniería en Computación*

Este repositorio contiene la implementación de un conjunto de herramientas para el análisis empírico de algoritmos de ordenamiento y la resolución optimizada de problemas geométricos. El proyecto destaca por una arquitectura modular, uso de principios **SOLID**, tipado estático y visualizaciones interactivas.

-----

## Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Características Técnicas](#características-técnicas)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Instalación y Requisitos](#instalación-y-requisitos)
5. [Módulos y Uso](#módulos-y-uso)
      - [Benchmarks de Ordenamiento](#1-benchmarks-de-ordenamiento)
      - [Desafío Geométrico (Triángulo de Área Máxima)](#2-desafío-geométrico-triángulo-de-área-máxima)
6. [Análisis de Complejidad](#análisis-de-complejidad)
7. [Autor](#autor)

-----

## Descripción General

El objetivo de este proyecto es demostrar la aplicación práctica de conceptos teóricos de complejidad algorítmica. Se divide en dos grandes componentes:

1. **Motor de Benchmarking:** Un comparador de algoritmos de sorting ($O(n^2)$ vs $O(n \log n)$) con medición de tiempos precisa y visualización en consola.
2. **Geometría Computacional:** Resolución del problema "Triángulo de Área Máxima" en una nube de puntos, comparando una solución de **Fuerza Bruta** contra una optimización basada en **Convex Hull (Cierre Convexo)**.

-----

## Características Técnicas

- **Arquitectura Modular:** Separación estricta entre Lógica (`algoritmos`), Orquestación (`runner`) y Utilidades (`utils`)
- **Código "Pythonico":** Uso extensivo de `Type Hinting`, `Context Managers` y `List Comprehensions`.
- **Concurrencia:** Implementación de hilos (`threading`) para animaciones de carga (Spinners) sin bloquear el procesamiento principal.
- **Visualización Gráfica:** Integración con `Matplotlib` para la verificación visual de soluciones geométricas.
- **Interfaz de Consola (CLI):** Salidas formateadas con `Colorama` para una experiencia de usuario profesional.

-----

## Estructura del Proyecto

```plaintext
DISENOANALISIALGORTIMOS
└───src
    │   main.py                     # Punto de entrada opcional
    │
    ├───algoritmos                  # Lógica pura y matemática
    │   │   _config.py              # Configuración global (Singleton)
    │   │   benchmarks.py           # Motor de medición de tiempos
    │   │   max_area_triangle.py    # Lógica: Convex Hull vs Brute Force
    │   │   __init__.py
    │
    ├───runner                      # Orquestadores y Controladores
    │   │   _config.py              # Configuración global (Singleton)
    │   │   run_benchmarks.py       # Driver para Sorting
    │   │   run_challenge_triangle.py # Driver para Geometría
    │   │   ui.py                   # Utilidades de UI (Spinner)
    │   │   __init__.py             # API Pública del paquete runner
    │
    └───utils                       # Herramientas transversales
    │   │   _config.py              # Configuración global (Singleton)
        │   data_generator.py       # Generador de datasets (Numpy)
        │   io_handlers.py          # Manejo de archivos (Input/Output)
        │   sorting.py              # Implementación de algoritmos de ordenamiento
        │   visualizer.py           # Motor de gráficos (Matplotlib)
        │   __init__.py
```

-----

## Instalación y Requisitos

Se recomienda usar un entorno virtual.

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/tu-repo.git
    cd DISENOANALISIALGORTIMOS
    ```

2. **Instalar dependencias:**

    ```bash
    pip install numpy colorama matplotlib
    ```

-----

## Módulos y Uso

### 1\. Benchmarks de Ordenamiento

Ejecuta una comparativa de rendimiento entre algoritmos clásicos (Bubble, Insertion, Selection) y eficientes (Quick, Merge, Heap, Shell).

**Comando:**

```bash
python -m src.runner.run_benchmarks
```

**Salida esperada:**
Una tabla dinámica en consola mostrando los tiempos de ejecución para diferentes tamaños de entrada ($N=100, 1000, 5000...$).

### 2\. Desafío Geométrico (Triángulo de Área Máxima)

Resuelve el problema de encontrar los 3 postes que forman el triángulo de mayor área dado un archivo de coordenadas.

**Comando:**

```bash
python -m src.runner.run_challenge_triangle
```

**Flujo de ejecución:**

1. Lee coordenadas desde `resources/campo.in`.
2. Ejecuta la **Optimización (Convex Hull)**.
3. Ejecuta **Fuerza Bruta** (si $N \le 500$) para validar la solución.
4. Genera un gráfico interactivo mostrando la nube de puntos y el triángulo solución.
5. Guarda el resultado en `resources/campo.out`.

-----

## Análisis de Complejidad

### Algoritmos de Ordenamiento

| Algoritmo | Caso Promedio | Comentario |
| :--- | :--- | :--- |
| **Bubble Sort** | $O(n^2)$ | Inviable para $N > 10,000$. |
| **Quick Sort** | $O(n \log n)$ | Alta eficiencia en memoria (in-place). |
| **Merge Sort** | $O(n \log n)$ | Estable, pero requiere memoria extra. |
| **Counting Sort** | $O(n + k)$ | Lineal, el más rápido para enteros en rango acotado. |

### Problema del Triángulo

- **Fuerza Bruta:** $O(n^3)$. Requiere iterar todas las combinaciones posibles de 3 puntos.
        - *Impacto:* Para $N=500$, toma \~9 segundos. Para $N=100,000$, tardaría años.
- **Optimización (Convex Hull + Monotone Chain):** $O(n \log n + h^3)$.
        - *Impacto:* Reduce el espacio de búsqueda de $N$ (todos los puntos) a $h$ (puntos en el perímetro).
        - *Resultado:* Tiempos menores a **0.002 segundos** para los mismos 500 puntos.

-----

## Autor

**[Tu Nombre Completo]**

- **Matrícula/ID:** [Tu Matrícula]
- **Carrera:** Ingeniería en Computación
- **Materia:** Diseño y Análisis de Algoritmos
- **Semestre:** [Quinto semestre. 2026-1]

-----

*Desarrollado como parte de la evaluación académica final.*
