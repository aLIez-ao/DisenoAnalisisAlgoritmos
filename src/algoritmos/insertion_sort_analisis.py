"""
Análisis: Insertion sort con búsqueda binaria para encontrar la posición de inserción
---------------------------------------------------------------------------------
Planteamiento:
  - En el insertion sort estándar, para insertar el elemento i-ésimo se hace
    una búsqueda lineal (hacia la izquierda) para localizar la posición correcta;
    eso conlleva O(i) comparaciones y O(i) desplazamientos en el peor caso.
  - Si en lugar de la búsqueda lineal usamos una búsqueda binaria para
    encontrar la posición correcta entre los i elementos ya ordenados, reducimos
    el número de comparaciones a O(log i) para esa etapa de búsqueda.

Efecto sobre la complejidad temporal (peor caso)
  - Comparaciones:
      Para cada i desde 1 hasta n, la búsqueda binaria hace O(log i) comparaciones.
      Sumando: Σ_{i=1..n} O(log i) = O(n log n) comparaciones en total.
  - Desplazamientos (movimientos de elementos en el arreglo):
      Incluso si sabemos la posición mediante búsqueda binaria, en un arreglo
      (estructura contigua) hay que desplazar en el peor caso O(i) elementos
      para abrir hueco e insertar el elemento.
      Sumando: Σ_{i=1..n} O(i) = O(n^2) movimientos en total.
  - Conclusión (peor caso): la complejidad temporal sigue siendo O(n^2).
      La búsqueda binaria reduce el número de comparaciones (de O(n^2) a O(n log n))
      pero **no** elimina los desplazamientos, que dominan el coste asintótico.

Casos particulares (mejor y promedio)
  - Mejor caso (entrada ya ordenada): ambos algoritmos son O(n) si se diseñan
    para detectar que no hay desplazamientos (insertion sort es adaptativo).
  - Promedio: la reducción de comparaciones puede mejorar el tiempo real, pero
    los desplazamientos siguen manteniendo la complejidad cuadrática asintótica.

Practicidad de implementar esta versión (ventajas y desventajas)
  - Ventajas prácticas:
      * Menos comparaciones: útil cuando comparar elementos es muy caro
        (por ejemplo, comparaciones profundas de objetos, costosas operaciones
         de comparación, o cuando comparar implica I/O).
      * Fácil de implementar: la búsqueda binaria para hallar índice es sencilla.
      * Mantiene la estabilidad del insertion sort si se elige correctamente
        cómo romper empates (por ejemplo, insertar después de iguales).
  - Desventajas/práctica en arrays:
      * Los desplazamientos siguen siendo el principal coste: para arreglos
        grandes no se gana en notación asintótica.
      * El coste en tiempo real puede mejorar solo moderadamente; en muchos lenguajes
        la sobrecarga adicional (llamadas a funciones de búsqueda binaria, cálculos
        de índices) puede reducir la ganancia.
  - Estructuras alternativas:
      * Si usamos una estructura que permita inserciones en O(log n) o O(1) y
        búsquedas por posición eficientes (p. ej. árboles balanceados, listas
        enlazadas con índices especiales, o una estructura con acceso aleatorio + 
        desplazamientos amortizados), entonces sí se pueden obtener mejoras
        reales. Ejemplos:
          - Mantener los datos en un árbol binario equilibrado → ordenación por
            inserción en árbol da O(n log n) en tiempo.
          - Usar un arreglo de bloques (gap buffer) o una estructura con
            inserciones amortizadas puede disminuir el coste de movimientos.
      * En listas enlazadas simples la búsqueda binaria es impracticable porque
        no hay acceso aleatorio O(1) a la mitad; la búsqueda binaria exige
        acceso aleatorio para ser eficiente.

Recomendación práctica
  - Para arreglos pequeños o parcialmente ordenados: el insertion sort modificado
    (con búsqueda binaria) puede ser útil porque reduce comparaciones y es
    sencillo; sigue siendo una buena elección por su comportamiento adaptativo.
  - Para arreglos grandes donde la eficiencia importa: preferir algoritmos
    O(n log n) que no requieran desplazamientos masivos (merge sort, heapsort,
    quicksort bien optimizado, o construcción con estructuras auxiliares).
  - Si las comparaciones son la operación dominante y muy costosa, la versión
    con búsqueda binaria puede ser justificada aun cuando los desplazamientos
    sigan siendo O(n^2) en teoría.

Breve justificación cuantitativa
  - Comparaciones totales ≈ O(n log n).
  - Movimientos totales ≈ O(n^2).
  - Tiempo total dominado por movimientos → O(n^2) en el peor caso.

Ejemplo de idea (pseudoestructura de algoritmo)
  for i in range(1, n):
      key = A[i]
      # buscar posición con búsqueda binaria en A[0:i]
      pos = binary_search_position(A, key, 0, i-1)
      # desplazar A[pos:i-1] una posición a la derecha (coste O(i-pos))
      shift_right(A, pos, i-1)
      A[pos] = key

Conclusión corta
  - La modificación mejora el número de comparaciones (de O(n^2) a O(n log n))
    pero **no cambia la complejidad asintótica total** en el peor caso sobre arreglos:
    el algoritmo sigue siendo O(n^2) por los desplazamientos. Su implementación
    es práctica en casos específicos (comparaciones caras, arreglos pequeños,
    entradas casi ordenadas), pero para grandes entradas es preferible usar
    algoritmos O(n log n) diseñados para evitar desplazamientos masivos.
"""
