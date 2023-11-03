"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
"""

if __name__ == "__main__":
    numero_ganador = []

    for n in range(6):
        numCorrecto = False
        while not numCorrecto:
            try:
                numero = int(input("Introduce el numero ganador: "))
                numero_ganador.append(numero)
                numCorrecto = True
            except ValueError:
                print("Introduce un número!!")

    print("Los números ganadores son: " + str(numero_ganador))