from src.ejercicio9 import contar_vocales

def test_contar_vocales():
    assert contar_vocales("hola") == {'a': 1, 'e': 0, 'i': 0, 'o': 1, 'u': 0}
    assert contar_vocales("supercalifragilisticoespialidoso") == {'a': 3, 'e': 2, 'i': 6, 'o': 3, 'u': 1}