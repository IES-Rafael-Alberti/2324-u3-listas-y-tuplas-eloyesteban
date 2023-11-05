"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

if __name__ == "__main__":
    
    lista_numeros = [1,2,3,4,5,6,7,8,9,10]
    lista_numeros.reverse()

    for numero in lista_numeros:
        print(numero, end = ", ")

