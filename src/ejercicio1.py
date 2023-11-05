"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla. 
"""

#Función donde asignamos la lista
def obtener_asignaturas():
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    return asignaturas

if __name__ == "__main__":

    #Entrada

    #Procesar

    listado_asignaturas = obtener_asignaturas() #Llamada a la función

    #Salida

    print("Asignaturas del curso:")
    for asignatura in listado_asignaturas:
        print(asignatura)