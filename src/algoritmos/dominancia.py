from typing import List, Tuple, Any, Sequence

# ==================== Funciones Publicas ================================

#  FUERZA BRUTA (Iterativo) O(N^2) 
def dominancia_nn(puntos_entrada: Sequence[Tuple[float, float]]) -> List[List[Any]]:
    """
    Calcula el rango de cada punto comparándolo contra todos los demás.
    
    Args:
        puntos_entrada (list): Lista de tuplas (x, y).
        
    Returns:
        list: Lista de listas [x, y, id_original, rango].
    """
    # Estructura: [x, y, id_original, rango] agregando un ID y el rango
    puntos = [[p[0], p[1], i, 0] for i, p in enumerate(puntos_entrada)]
    n = len(puntos)
    
    # Comparar cada punto con todos los demás
    for i in range(n):
        px, py = puntos[i][0], puntos[i][1]
        
        for j in range(n):
            if i == j: 
                continue
            
            qx, qy = puntos[j][0], puntos[j][1]
            
            # Condición de dominancia: Q domina a P si sus dos coordenadas son mayores o iguales
            if qx >= px and qy >= py:
                puntos[i][3] += 1
                
    return puntos


#  DIVIDE Y VENCERÁS (Optimizado) O(N log N) 
def dominancia_nlogn(puntos_entrada: Sequence[Tuple[float, float]]) -> List[List[Any]]:
    """
    Calcula el rango de cada punto comparándolo contra todos los demás.
    
    Args:
        puntos_entrada (list): Lista de tuplas (x, y).
        
    Returns:
        list: Lista de listas [x, y, id_original, rango].
    """
    # Estructura: [x, y, id_original, rango] agregando un ID y el rango
    datos = [[p[0], p[1], i, 0] for i, p in enumerate(puntos_entrada)]
    
    # Ordenar por X descendente para garantizar que la parte izquierda siempre tenga X mayor
    datos.sort(key=lambda x: x[0], reverse=True)
    
    # Llamar al mergesort modificado que también cuenta dominancias
    resultado = _mergesort_y_conteo(datos)
    
    # Reordenamos por ID original para que coincida con la entrada
    resultado.sort(key=lambda x: x[2])
    return resultado


# ==================== Funciones Privadas ================================

def _mergesort_y_conteo(arreglo: List[List[Any]]) -> List[List[Any]]:
    """
    Implementación personalizada de Merge Sort.
    Ordena el arreglo por la coordenada Y de forma DESCENDENTE.
    Al mismo tiempo, cuenta las dominancias aprovechando el orden de X preexistente.
    """
    # Caso Base: Si la lista tiene 0 o 1 elemento, ya está ordenada.
    if len(arreglo) <= 1: return arreglo
    
    # División del arreglo en mitades
    mitad = len(arreglo) // 2
    izquierda = arreglo[:mitad]
    derecha = arreglo[mitad:]
    
    # Recursión sobre ambas mitades
    izquierda = _mergesort_y_conteo(izquierda)
    derecha = _mergesort_y_conteo(derecha)
    
    # Mezcla con conteo de dominancias
    return _merge_y_contar(izquierda, derecha)


def _merge_y_contar(izq: List[List[Any]], der: List[List[Any]]) -> List[List[Any]]:
    """
    Mezcla dos arreglos ordenados por Y (descendente).
    Cuenta cuántos elementos de 'izq' dominan a elementos de 'der'.
    """
    # Lista resultado final y Cantidad de puntos en 'izq' como posibles dominadores
    resultado = []
    dominadores_acumulados = 0 
    
    # Punteros de recorrido para ambas listas
    i = 0
    j = 0
    
    # Mezcla clásica integrando conteo
    while i < len(izq) and j < len(der):
       # Si el punto de izquierda tiene Y mayor o igual, domina y aumenta acumulador
        if izq[i][1] >= der[j][1]:
            dominadores_acumulados += 1
            resultado.append(izq[i])
            i += 1
        else:
            # El punto de derecha es dominado por todos los dominadores acumulados hasta ahora
            der[j][3] += dominadores_acumulados
            der[j][3] += dominadores_acumulados
            resultado.append(der[j])
            j += 1
            
    # Agregar remanentes de izq, der y actualizar dominancias
    while i < len(izq):
        resultado.append(izq[i])
        i += 1
        
    while j < len(der):
        der[j][3] += dominadores_acumulados
        resultado.append(der[j])
        j += 1
        
    return resultado
