# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:22:48 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.9: Funciones de la biblioteca

Modificá tu programa costo_camion.py para que use el módulo csv para leer
los archivos CSV y probalo en un par de los ejemplos anteriores.

"""

# Importamos bibliotecas
import csv

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.9: Funciones de la biblioteca\n')

# Declaración de variables globales
costo = True
nombre_archivo = '../Data/camion.csv'

def costo_camion(nombre_archivo):
    # Declaración de variables locales
    precio = 0.00
    # Abrimos el archivo con el que vamos a trabajar
    f = open(nombre_archivo, 'rt')
    # Guardamos la primera linea, encabezado
    rows = csv.reader(f)
    header = next(rows)
    # Imprimimos el encabezado
    print('El encabezado del archivo es:', header)
    
    # Recorremos las filas del archivo
    for row in rows:
        print(row)
        precio += float(row[1]) * float(row[2])
    
    # Cerramos el archivo con el que trabajamos
    f.close()
    
    return(precio)

costo = costo_camion(nombre_archivo)
# Imprimimos el resultado de la suma total de cajones * precio
print('El precio de todos los cajones es:', round(costo, 2))


"""
RESULTADO:


 
"""