"""
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica. 
"""

def calcular_media_desviacion(muestra):
    muestra = muestra.split(',')
    n = len(muestra)
    muestra = [int(num) for num in muestra]
    media = sum(muestra) / n

    # Calcular la desviación 
    sum1 = sum((x - media) ** 2 for x in muestra)
    desviacion_tipica = (sum1 / (n - 1)) ** 0.5

    return media, desviacion_tipica

#Entrada
muestra = input("Introduce una muestra de números separados por comas: ")

#Procesar

media, desviacion_tipica = calcular_media_desviacion(muestra)

#Salida

print('La media es', media, 'y la desviación típica es', desviacion_tipica)

