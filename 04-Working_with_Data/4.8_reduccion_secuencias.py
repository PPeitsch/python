# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 05:09:13 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 4.8: Reducción de secuencias
Calculá el costo total de la carga del camión en un solo comando.

"""

# Importamos bibliotecas
import csv
import copy

# Definimos variables globales
nombre_archivo = '../Data/camion.csv'
precios = {}
camion = list()

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 4.8: Reducción de secuencias.\n')

def leer_camion(nombre_archivo):
    # Declaración de variables locales
    lista_temp = []
    lote = {}
    
    # Recorremos las filas del archivo
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            try:
                lote[encabezado[0]] = fila[0]
                lote[encabezado[1]] = int(fila[1])
                lote[encabezado[2]] = float(fila[2])
                lista_temp.append(copy.deepcopy(lote))
            except ValueError:
                print(f'No pude interpretar: {fila}')
    return(lista_temp)

camion = leer_camion(nombre_archivo)

valor = sum([s['cajones'] * s['precio'] for s in camion])
print(f'La suma de cajones * precio de la lista:\n{valor}')

#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 4.8: Reducción de secuencias.

La suma de cajones * precio de la lista:
47671.15

"""