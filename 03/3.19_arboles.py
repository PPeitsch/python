# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 05:40:29 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.19: Determinar las especies en un parque

"""
# Importamos bibliotecas
import copy
import csv

# Definimos variables globales
nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
espacio_verde = "GENERAL PAZ"

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

def especies(lista_arboles):
    lista = []
    cadena = ''
    
    # Guardo los nombres de los arboles
    for i in range(len(lista_arboles)):
        cadena = lista_arboles[i]['nombre_com']
        lista.append(copy.deepcopy(cadena))
    # Elimino duplicados
    sin_duplicados = set(lista)
    return sin_duplicados
    

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.19: Determinar las especies en un parque.\n')

lista = leer_parque(nombre_archivo, espacio_verde)
especies_presentes = especies(lista)

print(f'La lista contiene información de {len(lista)} árboles')
print(f'La lista de especies en el espacio verde {espacio_verde} contiene {len(especies_presentes)} árboles')

#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.19: Determinar las especies en un parque.

La lista contiene información de 690 árboles
La lista de especies en el espacio verde GENERAL PAZ contiene 81 árboles


"""