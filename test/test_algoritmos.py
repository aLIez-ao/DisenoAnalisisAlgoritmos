from src.algoritmos import existe_par_suma_k, existe_par_suma_k_optimizado


def test_existe_par():
    arreglo = [1, 2, 3, 4]
    k = 5
    assert existe_par_suma_k(arreglo, k) == True
    assert existe_par_suma_k_optimizado(arreglo, k) == True


def test_no_existe_par():
    arreglo = [1, 2, 3]
    k = 10
    assert existe_par_suma_k(arreglo, k) == False
    assert existe_par_suma_k_optimizado(arreglo, k) == False
