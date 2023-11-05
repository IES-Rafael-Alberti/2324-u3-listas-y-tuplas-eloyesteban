"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal. 
"""

def contar_vocales(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    resultados = {}

    for vocal in vocales:
        repeticiones = 0
        for letra in palabra:
            if letra == vocal:
                repeticiones += 1
        resultados[vocal] = repeticiones

    return resultados

if __name__ == "__main__":

    #Entrada

    palabra = input("Introduce una palabra: ")

    #Procesar
    resultado = contar_vocales(palabra)

    #Salida

    for vocal, repeticiones in resultado.items():
        print(f"La vocal {vocal} aparece {repeticiones} veces")
