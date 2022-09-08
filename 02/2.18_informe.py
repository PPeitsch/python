# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:54:02 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.18: Balances

"""
# Importamos bibliotecas
import csv
import sys
from pprint import pprint
import copy

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.18: Balances.\n')

# Declaración de variables globales
precios = {}
lista = []
precio = 0.00
total = 0.00
fruta = ''

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

def leer_precios(nombre_archivo):
    # Declaración de variables locales
    lote = {}
    
    # Recorremos las filas del archivo
    with open(nombre_archivo, "rt", encoding="utf-8") as f:
        filas = csv.reader(f)
        for fila in filas:
            try:
                lote[fila[0]] = float(fila[1])
            except IndexError:
                print(f'El archivo {nombre_archivo} contiene línea sin datos. Se ignora.')
            except ValueError:
                print(f'No pude interpretar: {fila}')
    return(lote)

try:
    nombre_archivo = '../Data/camion.csv'
    lista = leer_camion(nombre_archivo)

except FileNotFoundError:
    print('Error: No se encontró el archivo:', nombre_archivo)

try:
    nombre_archivo = '../Data/precios.csv'
    precios = leer_precios(nombre_archivo)

except FileNotFoundError:
    print('Error: No se encontró el archivo:', nombre_archivo)
    
for a in range(len(lista)):
    diferencia = lista[a]['precio'] - precios[lista[a]['nombre']]
    total += lista[a]['cajones'] * abs(diferencia)

print('El balance total es:', total)

#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.18: Balances.

El archivo ../Data/precios.csv contiene línea sin datos. Se ignora.
El balance total es: 15314.95

"""