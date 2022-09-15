# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:54:02 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.9: La función zip()

"""
# Importamos bibliotecas
import csv
import sys

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.9: La función zip()\n')

# Declaración de variables globales
costo_total = True

def costo_camion(nombre_archivo):
    # Declaración de variables locales
    costo_total = 0.00
    # Abrimos el archivo con el que vamos a trabajar
    f = open(nombre_archivo, 'rt')
    filas = csv.reader(f)
    encabezados = next(filas)
    
    # Recorremos las filas del archivo
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        print(record)
        try:
            n_cajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += n_cajones * precio
            
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    
    # Cerramos el archivo con el que trabajamos
    f.close()
    
    return(costo_total)


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
try:
    costo_total = costo_camion(nombre_archivo)

except FileNotFoundError:
    try:
        nombre_archivo = '../Data/camion.csv'
        print('Archivo no encontrado. Se usa por defecto:', nombre_archivo)
        costo = costo_camion(nombre_archivo)
    except FileNotFoundError:
        print('Error: No se encontró el archivo:', nombre_archivo)

# Imprimimos el resultado de la suma total de cajones * precio
print('El precio de todos los cajones es:', round(costo_total, 2))


#%%
"""
RESULTADO 1:

python 3.9_funcion_zip.py ../Data/fecha_camion.csv
    
Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.9: La función zip()

{'nombre': 'Lima', 'fecha': '6/2/2020', 'hora': '9:50am', 'cajones': '100', 'precio': '32.2'}
{'nombre': 'Naranja', 'fecha': '5/26/2020', 'hora': '4:20pm', 'cajones': '50', 'precio': '91.1'}
{'nombre': 'Caqui', 'fecha': '5/23/2020', 'hora': '1:30pm', 'cajones': '150', 'precio': '103.44'}
{'nombre': 'Mandarina', 'fecha': '5/27/2020', 'hora': '10:30am', 'cajones': '200', 'precio': '51.23'}
{'nombre': 'Durazno', 'fecha': '6/1/2020', 'hora': '10:45am', 'cajones': '95', 'precio': '40.37'}
{'nombre': 'Mandarina', 'fecha': '6/3/2020', 'hora': '12:05pm', 'cajones': '50', 'precio': '65.1'}
{'nombre': 'Naranja', 'fecha': '6/9/2020', 'hora': '3:15pm', 'cajones': '100', 'precio': '70.44'}
El precio de todos los cajones es: 47671.15

"""

#%%

"""
RESULTADO 2:

python 3.9_funcion_zip.py ../Data/fecha_cam.csv

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.9: La función zip()


Archivo no encontrado. Se usa por defecto: ../Data/camion.csv
{'nombre': 'Lima', 'cajones': '100', 'precio': '32.2'}
{'nombre': 'Naranja', 'cajones': '50', 'precio': '91.1'}
{'nombre': 'Caqui', 'cajones': '150', 'precio': '103.44'}
{'nombre': 'Mandarina', 'cajones': '200', 'precio': '51.23'}
{'nombre': 'Durazno', 'cajones': '95', 'precio': '40.37'}
{'nombre': 'Mandarina', 'cajones': '50', 'precio': '65.1'}
{'nombre': 'Naranja', 'cajones': '100', 'precio': '70.44'}
El precio de todos los cajones es: 47671.15

"""