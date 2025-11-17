"""
Problema del triángulo de mayor área con postes en un campo
-----------------------------------------------------------

Descripción general:
Dado un conjunto de puntos en el plano (máximo 500), se debe encontrar
el triángulo de mayor área posible que pueda formarse seleccionando tres
de esos puntos. La salida consiste en las coordenadas de esos tres postes.

------------------------------------------
1. Solución por fuerza bruta (Brute Force)
------------------------------------------

Idea:
- Probar todas las combinaciones posibles de 3 puntos entre los N postes.
- Para cada tripleta (A, B, C), calcular el área del triángulo usando la
  fórmula de determinante:

      Area = | x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2) | / 2

- Conservar el máximo.

Número de combinaciones:
- El número de triángulos posibles es C(N, 3) = N(N - 1)(N - 2) / 6

Cota superior:
--------------
El algoritmo visita todas las combinaciones → tiempo O(N^3)
Cálculo de área → O(1)

Por lo tanto, la complejidad de la solución por fuerza bruta es:
                           O(N^3)

Como N ≤ 500:
  C(500,3) ≈ 20,708,500 → es pesado pero posible en tiempo razonable en C++,
  más lento en Python pero aún factible con optimizaciones.


------------------------------------------
2. Búsqueda de una mejora (optimización)
------------------------------------------

Observación:
- El triángulo de mayor área formado por puntos en un plano SIEMPRE tiene
  a sus vértices sobre la envolvente convexa (convex hull).

Motivo:
- Cualquier punto interior no puede formar un triángulo que supere en área
  a uno cuyos vértices están en la envolvente convexa.

Entonces:
1. Calcular la envolvente convexa de los puntos.  
   Algoritmos recomendados:
     • Monotone chain (O(N log N))
     • Graham scan (O(N log N))

2. Luego, solo probar triángulos formados por puntos del hull.
   Si H es el número de puntos en la envolvente convexa, entonces:
     - Peor caso: H ≈ N (por ejemplo, puntos en círculo)
     - Caso común: H << N

3. Usar el método de "rotating calipers" para encontrar el triángulo
   de área máxima en tiempo O(H²), mucho más eficiente que O(N³).

Cotas superiores:
-----------------
Convex hull: O(N log N)
Rotating calipers: O(H²)
Total: O(N log N + H²)

En el peor caso → H = N:
   → O(N log N + N²)
   Mucho mejor que O(N³)

En el caso típico → H muy pequeño:
   → casi O(N log N)


------------------------------------------
3. Conclusión general
------------------------------------------

• Método de fuerza bruta:
     - Complejo: O(N³)
     - Fácil de implementar.
     - Funciona para N ≤ 500, pero lento en Python.

• Método optimizado:
     - Usa convex hull + rotating calipers.
     - Complejidad: O(N log N + H²)
     - Mucho más rápido en la práctica.
     - Reduce el trabajo a los puntos relevantes del perímetro.

------------------------------------------
4. Pseudocódigo simplificado (optimizado)
------------------------------------------

1. Leer lista de puntos
2. Obtener envolvente convexa con monotone chain → hull[]
3. maxArea = 0
4. Para cada i en hull:
       Para cada j > i en hull:
           Aplicar rotating calipers para encontrar k que maximiza el área
           Actualizar maxArea y los vértices
5. Imprimir los 3 postes en campo.out

------------------------------------------
5. Fórmula del área usada
------------------------------------------

def area(A, B, C):
    return abs(
        A.x * (B.y - C.y) +
        B.x * (C.y - A.y) +
        C.x * (A.y - B.y)
    ) / 2


"""
