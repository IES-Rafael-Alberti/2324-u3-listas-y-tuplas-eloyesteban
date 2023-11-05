"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir. 
"""

if __name__ == "__main__":
    
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    
    for i in range(4,-1,-1):

        nota = float(input("Introduce un la nota de " + asignaturas[i] + ":"))
        if nota >= 5:
            asignaturas.pop(i)

    print(asignaturas)