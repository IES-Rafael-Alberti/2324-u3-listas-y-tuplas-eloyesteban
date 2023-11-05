from src.ejercicio8 import es_palindromo

def test_es_palindromo():

    assert es_palindromo("ana") == True
    assert es_palindromo("hola") == False