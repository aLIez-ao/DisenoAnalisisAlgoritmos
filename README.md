# Diseño y Análisis de Algoritmos

Este proyecto contiene implementaciones de varios algoritmos clásicos en Python, tanto **iterativos** como **recursivos**, y herramientas para probarlos con **datos generados dinámicamente**.

---

## Estructura del proyecto

```plaintext
Algortimos
│
└───src
    │   main.py
    │
    ├───algoritmos
    │       dominancia.py
    │       iterativos.py
    │       ordenamiento.py
    │       recursivos.py
    │       __init__.py
    │
    ├───runner
    │       run_dominancia.py
    │       run_iterativos.py
    │       run_ordenamiento.py
    │       run_recursivos.py
    │       __init__.py
    │
    ├───tmp
    │       tmp.py
    │
    └───utils
            generador_datos.py
            visualizacion.py
            __init__.py
```

## Funcionalidades principales

### 1. Suma de dígitos

- `suma_digitos_iterativo(n)` → Calcula la suma de los dígitos de `n` de forma iterativa.
- `suma_digitos_recursivo(n)` → Calcula la suma de los dígitos de `n` de forma recursiva.

### 2. Máximo Común Divisor (MCD)

- `mcd_iterativo(a, b)` → Calcula el MCD de `a` y `b` usando el algoritmo de Euclides iterativo.
- `mcd_recursivo(a, b)` → Calcula el MCD de `a` y `b` usando el algoritmo de Euclides recursivo.

### 3. Ejecución visual

- Funciones `ejecutar_*` que muestran **pasos y resultados** en consola con colores (`colorama`) para facilitar la comprensión.

### 4. Generación de datos dinámicos

- Números aleatorios grandes, medianos y pequeños.
- Pares de números para MCD.
- Arreglos, listas, pilas y colas generadas aleatoriamente para pruebas de algoritmos.

## Cómo ejecutar

1. **Clonar el repositorio**

   ```bash
   git clone <URL_DEL_REPO>
   cd <NOMBRE_DEL_REPO>
   ```

2. **Activar el entorno virtual**

   ```bash
   # Windows PowerShell
   & .venv\Scripts\Activate.ps1

   # Linux/macOS
   source .venv/bin/activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el script principal**

   ```bash
   python src/main.py
   ```

   - Por defecto, `main.py` ejecuta el algoritmo definido en `algoritmo_ejecutar`.
   - Puedes cambiar `algoritmo_ejecutar` a cualquiera de las funciones disponibles:

   ```python
   "suma_digitos_iterativo"
   "mcd_iterativo"
   "suma_digitos_recursivo"
   "mcd_recursivo"
   "ordenamiento_mergesort"
   "ordenamiento_quicksort"
   ```

## Dependencias

Archivo `requirements.txt`:

```text
colorama==0.4.6
numpy==2.3.2
paquete==0.2
```

- `colorama` → Para colores en consola y mejor visualización de resultados.
- `numpy` → Para operaciones con arreglos.
- `paquete` → Dependencia personalizada (si aplica).

## Notas

- El entorno virtual `.venv` **se comparte entre ramas**, pero cada rama puede tener su propio `requirements.txt`.
- Para actualizar las dependencias del entorno en una rama:

  ```bash
  pip freeze > requirements.txt
  ```
  