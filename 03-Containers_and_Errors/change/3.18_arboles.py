# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 05:09:33 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.18: Lectura de los árboles de un parque

"""
# Importamos bibliotecas
import copy
import csv

# Definimos variables globales
nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

# Definición de funciones
def leer_parque(nombre_archivo, parque):
    lista = []
    dic = dict()
    
    # Abrimos el archivo con el que vamos a trabajar
    f = open(nombre_archivo, 'rt', encoding="utf8")
    filas = csv.reader(f)
    encabezados = next(filas)
    
    # Recorremos las filas del archivo
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        if record['espacio_ve'] == parque:
            dic = record
            lista.append(copy.deepcopy(dic))
    
    return lista
    
    # Cerramos el archivo con el que trabajamos
    f.close()
    
    return lista

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.18: Lectura de los árboles de un parque.\n')

lista = leer_parque(nombre_archivo, "GENERAL PAZ")
print(f'La lista contiene información de {len(lista)} árboles')

#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.18: Lectura de los árboles de un parque.

La lista contiene información de 690 árboles

"""