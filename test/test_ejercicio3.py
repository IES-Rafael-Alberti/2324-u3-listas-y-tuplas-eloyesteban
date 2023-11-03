from src.ejercicio3 import obtener_asignaturas

def test_obtener_asignaturas():
    assert obtener_asignaturas() == ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
