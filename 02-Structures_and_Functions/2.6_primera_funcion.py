# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:42:44 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.6: Transformar un script en una función

Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2
de la sección anterior) en una función costo_camion(nombre_archivo).
Esta función recibe un nombre de archivo como entrada, lee la información
sobre los cajones que cargó el camión y devuelve el costo de la carga de
frutas como una variable de punto flotante.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.6: Transformar un script en una función\n')

# Declaración de variables globales
costo = True
nombre_archivo = '../Data/camion.csv'

def costo_camion(nombre_archivo):
    # Declaración de variables locales
    precio = 0.00
    # Abrimos el archivo con el que vamos a trabajar
    f = open(nombre_archivo, 'rt')
    # Guardamos la primera linea, encabezado
    headers = next(f).split(',')
    # Imprimimos el encabezado
    print('El encabezado del archivo es:', headers)
    
    # Recorremos las filas del archivo
    for line in f:
        row = line.split(',')
        precio += float(row[1].rstrip("\\n")) * float(row[2].rstrip("\\n"))
    
    # Cerramos el archivo con el que trabajamos
    f.close()
    
    return(precio)

costo = costo_camion(nombre_archivo)
# Imprimimos el resultado de la suma total de cajones * precio
print('El precio de todos los cajones es:', round(costo, 2))


"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.6: Transformar un script en una función

El encabezado del archivo es: ['nombre', 'cajones', 'precio\n']
El precio de todos los cajones es: 47671.15
 
"""