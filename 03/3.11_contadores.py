# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:46:15 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.11 Contadores
Vamos a usar un contador (objeto Counter) para contar cajones de frutas.

"""
# Importamos bibliotecas
from collections import Counter
import csv

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.11 Contadores.\n')

# Declaración de variables globales
combinada = Counter()
nombre_archivo1 = '../Data/camion.csv'
nombre_archivo2 = '../Data/camion2.csv'

def tenencias1(nombre_archivo1):
    
    # Recorremos las filas del archivo
    with open(nombre_archivo1, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        tenencias1 = Counter()
        for fila in filas:
            try:
                tenencias1[fila['nombre']] += fila['cajones']
            except ValueError:
                print(f'Fila {fila}: No pude interpretar: {filas}')
    
    # Cerramos el archivo con el que trabajamos
    filas.close()
    
    return(tenencias1)

def tenencias2(nombre_archivo2):
    # Abrimos el archivo con el que vamos a trabajar
    camion2 = open(nombre_archivo2, 'rt')
    tenencias2 = Counter()
    
    for s in camion2:
        try:
            
            tenencias2[s['nombre']] += s['cajones']
        except ValueError:
            print(f'Fila {s}: No pude interpretar: {camion2}')
    
    # Cerramos el archivo con el que trabajamos
    camion2.close()
    
    return(tenencias2)

try:
    combinada = tenencias1(nombre_archivo1) + tenencias2(nombre_archivo2)
except FileNotFoundError:
    print('Error: No se encontró el archivo.')

# Imprimimos el resultado de la suma total de cajones * precio
print('Las tenencias de ambos camiones:', combinada)

#%%
"""
RESULDADO:



"""