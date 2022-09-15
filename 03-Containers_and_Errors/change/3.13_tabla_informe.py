# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 04:56:50 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.13: Recolectar datos

"""
# Importamos bibliotecas
import csv
import copy
from pprint import pprint

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.13: Recolectar datos.\n')

# Declaración de variables globales
informe = []

def leer_camion(nombre_archivo):
    # Declaración de variables locales
    lista_temp = []
    lote = {}
    try:
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
    except FileNotFoundError:
        print('No se encuentra el archivo:', nombre_archivo)
    return(lista_temp)

def leer_precios(nombre_archivo):
    # Declaración de variables locales
    lote = {}
    try:
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
    except FileNotFoundError:
        print('No se encuentra el archivo:', nombre_archivo)
    return(lote)

def hacer_informe(camion, precios):
    # Defino variables locales
    informe = []
    
    for a in range(len(camion)):
        try:
            lista = []
            lista.append(camion[a]['nombre'])
            lista.append(camion[a]['cajones'])
            lista.append(round(camion[a]['precio'], 2))
            lista.append(round(abs(camion[a]['precio'] - precios[camion[a]['nombre']]), 2))
            informe.append(copy.deepcopy(tuple(lista)))
        except ValueError:
            print(f'No pude interpretar: {a}')
    return(informe)

nombre_archivo1 = '../Data/camion.csv'
nombre_archivo2 = '../Data/precios.csv'
informe = hacer_informe(leer_camion(nombre_archivo1), leer_precios(nombre_archivo2))

# Imprimimos la lista entera
pprint(informe)


#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.13: Recolectar datos.

El archivo ../Data/precios.csv contiene línea sin datos. Se ignora.
[('Lima', 100, 32.2, 8.02),
 ('Naranja', 50, 91.1, 15.18),
 ('Caqui', 150, 103.44, 2.02),
 ('Mandarina', 200, 51.23, 29.66),
 ('Durazno', 95, 40.37, 33.11),
 ('Mandarina', 50, 65.1, 15.79),
 ('Naranja', 100, 70.44, 35.84)]

"""