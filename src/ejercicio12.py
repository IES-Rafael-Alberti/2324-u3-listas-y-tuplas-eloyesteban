"""
Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista. 
"""

def multiplicar_matrices(a, b):
    resultado = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][j] += a[i][k] * b[k][j]

    return resultado

if __name__ == "__main__":

    #Entrada

    a = ((1, 2, 3), (4, 5, 6))
    b = ((-1, 0), (0, 1), (1, 1))

    #Procesar

    resultado = multiplicar_matrices(a, b)

    for i in range(len(resultado)):
        resultado[i] = tuple(resultado[i])

    result = tuple(resultado)

    #Salida
    
    for i in range(len(resultado)):
        print(resultado[i])
