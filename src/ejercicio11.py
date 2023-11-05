"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar. 
"""
def producto_escalar(vector_a, vector_b):
    producto = 0
    for i in range(len(vector_a)):
        producto += vector_a[i] * vector_b[i]
    return producto

if __name__ == "__main__":

    #Entrada

    a = (1, 2, 3)
    b = (-1, 0, 2)

    #Procesar

    resultado = producto_escalar(a, b)

    #Salida

    print("El producto de los vectores", a, "y", b, "es", resultado)
