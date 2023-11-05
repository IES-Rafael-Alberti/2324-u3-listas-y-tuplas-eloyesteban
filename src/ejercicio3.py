"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario. 
"""
def obtener_asignaturas():
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    return asignaturas

if __name__ == "__main__":

    asignaturas = obtener_asignaturas()
    notas = []

    #Añadimos las notas a la lista
    
    numCorrecto = False
    
    for asignatura in asignaturas: 
        numCorrecto = False
        while not numCorrecto:
            try:
                nota = int(input("Qué nota tienes en " + asignatura + ":"))
                notas.append(nota)
                numCorrecto = True
            except ValueError:
                print("Introduce un número!!")

    for i in range(4):
        print("En " + asignaturas[i] + " tengo un " + str(notas[i]))