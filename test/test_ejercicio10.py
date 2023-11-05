from src.ejercicio10 import encontrar_minimo_maximo

def test_encontrar_minimo_maximo():

    precios = [50, 75, 46, 22, 80, 65, 8]
    assert encontrar_minimo_maximo(precios) == (8 , 80)