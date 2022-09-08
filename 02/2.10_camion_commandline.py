# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:34:54 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros

Copiá el contenido de costo_camion.py a un nuevo archivo llamado
camion_commandline.py que incorpore la lectura de parámetros
por línea de comando.

"""

# Importamos bibliotecas
import csv
import sys

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros\n')

# Declaración de variables globales
costo = True

def costo_camion(nombre_archivo):
    # Declaración de variables locales
    precio = 0.00
    # Abrimos el archivo con el que vamos a trabajar
    f = open(nombre_archivo, 'rt')
    # Guardamos la primera linea, encabezado
    rows = csv.reader(f)
    header = next(rows)
    
    # Recorremos las filas del archivo
    for row in rows:
        precio += float(row[1]) * float(row[2])
    
    # Cerramos el archivo con el que trabajamos
    f.close()
    
    return(precio)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
# Imprimimos el resultado de la suma total de cajones * precio
print('El precio de todos los cajones es:', round(costo, 2))

"""
RESULTADO:

C:\Users\Pablo\Desktop\Python\Clase02>python camion_commandline.py ../Data/camion.csv

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros

El precio de todos los cajones es: 47671.15
 
"""