"""
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios. 
"""

def encontrar_minimo_maximo(precios):
    minimo = maximo = precios[0]
    for precio in precios:
        if precio < minimo:
            minimo = precio
        elif precio > maximo:
            maximo = precio

    return minimo, maximo

if __name__ == "__main__":

    #Entrada

    precios = [50, 75, 46, 22, 80, 65, 8]
    
    #Procesar

    minimo, maximo = encontrar_minimo_maximo(precios)

    #Salida
    
    print("El mínimo es " + str(minimo) + "\nEl máximo es " + str(maximo))
 
