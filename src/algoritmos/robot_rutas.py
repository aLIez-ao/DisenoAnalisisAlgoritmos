"""
1. Técnicas de diseño de algoritmos:

a) Para determinar si existe un camino que permita al robot llegar del origen al
   destino sin pasar dos veces por la misma casilla, utilizaría la técnica de
   **Backtracking**, ya que permite explorar rutas posibles y retroceder cuando
   una ruta no conduce a la solución sin repetir casillas.

   Implementación (ejemplo en Python):

   def existe_camino(n, m):
       visitado = [[False]*m for _ in range(n)]

       def backtrack(x, y):
           if x == n-1 and y == m-1:
               return True
           if x < 0 or x >= n or y < 0 or y >= m or visitado[x][y]:
               return False

           visitado[x][y] = True
           # Mover derecha (avanza 3)
           if backtrack(x, y + 3):
               return True
           # Mover abajo (avanza 2)
           if backtrack(x + 2, y):
               return True

           visitado[x][y] = False
           return False

       return backtrack(0, 0)

b) Para determinar todos los caminos posibles del origen al destino usaría
   nuevamente **Backtracking**, ya que se requiere explorar exhaustivamente
   todas las rutas posibles y almacenar aquellas que lleguen a la meta sin
   repetir casillas.

   (La idea del algoritmo es similar, pero almacenando las rutas encontradas).
"""
