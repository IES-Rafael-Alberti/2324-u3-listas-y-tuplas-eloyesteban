from src.ejercicio11 import producto_escalar

def test_producto_escalar():

    a = (1, 2, 3)
    b = (-1, 0, 2)

    assert producto_escalar(a,b) == 5