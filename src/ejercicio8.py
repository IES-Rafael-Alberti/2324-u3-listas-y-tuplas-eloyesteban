"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo. 
"""


def es_palindromo(palabra):
    palabra = palabra.lower() 
    reversa_palabra = palabra[::-1]

    return palabra == reversa_palabra

if __name__ == "__main__":

    #Entrada

    palabra = input("Introduce una palabra: ")

    #Procesar

    resultado = es_palindromo(palabra)

    #Salida

    if resultado:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
