# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:04:15 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.2: Lectura de un archivo de datos

Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad
de cajones cargados en el camión, y un precio de compra por cada cajón de ese
grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea
las líneas, y calcule el precio pagado por los cajones cargados en el camión.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.2: Lectura de un archivo de datos\n')

# Declaración de variables
precio = 0.00
individual = 0.00

# Abrimos el archivo con el que vamos a trabajar
f = open('../Data/camion.csv', 'rt')
# Guardamos la primera linea, encabezado
headers = next(f).split(',')
# Imprimimos el encabezado
print('El encabezado del archivo es:', headers)

# Recorremos las filas del archivo
for line in f:
    row = line.split(',')
    precio += float(row[1].rstrip("\\n")) * float(row[2].rstrip("\\n"))

# Imprimimos el resultado de la suma total de cajones * precio
print('El precio de todos los cajones es:', round(precio, 2))


# Cerramos el archivo con el que trabajamos
f.close()

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.2: Lectura de un archivo de datos

El encabezado del archivo es: ['nombre', 'cajones', 'precio\n']
El precio de todos los cajones es: 47671.15
 
"""