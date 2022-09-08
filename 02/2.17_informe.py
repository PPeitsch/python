# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:54:02 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.17: Diccionarios como contenedores

"""
# Importamos bibliotecas
import csv
import sys
from pprint import pprint

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.17: Diccionarios como contenedores.\n')

# Declaración de variables globales
precios = {}
precio = 0.00
fruta = ''

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
                print('Linea sin datos')
            except ValueError:
                print(f'No pude interpretar: {fila}')
    return(lote)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/precios.csv'
try:
    precios = leer_precios(nombre_archivo)

except FileNotFoundError:
    print('Error: No se encontró el archivo:', nombre_archivo)

# Imprimimos el resultado
print('La lista completa es:')
pprint(precios)

fruta = input('Ingrese la fruta a buscar: ')

try:
    for a in range(len(precios)):
        precio = precios[fruta]
    print(f'El precio de {fruta} es: {precio}')
except KeyError:
    print(f'La fruta {fruta} no se encuentra en la lista')



#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.17: Diccionarios como contenedores.

Linea sin datos
La lista completa es:
{'Acelga': 29.26,
 'Ajo': 15.19,
 'Batata': 55.16,
 'Berenjena': 28.47,
 'Bruselas': 15.72,
 'Caqui': 105.46,
 'Cebolla': 58.99,
 'Cebollín': 57.1,
 'Cereza': 11.27,
 'Ciruela': 44.85,
 'Durazno': 73.48,
 'Espinaca': 52.61,
 'Frambuesa': 34.35,
 'Frutilla': 53.72,
 'Habas': 23.16,
 'Lechuga': 24.22,
 'Lima': 40.22,
 'Mandarina': 80.89,
 'Naranja': 106.28,
 'Papa': 69.35,
 'Puerro': 27.58,
 'Rabanito': 51.94,
 'Radicheta': 26.11,
 'Remolacha': 20.75,
 'Repollo': 49.16,
 'Rúcula': 36.9,
 'Tomate': 66.67,
 'Uva': 24.85,
 'Zanahoria': 49.74,
 'Zapallo': 24.79}

Ingrese la fruta a buscar: tomato
La fruta tomato no se encuentra en la lista

...

Ingrese la fruta a buscar: Rúcula
El precio de Rúcula es: 36.9

"""