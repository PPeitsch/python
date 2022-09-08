# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 06:00:17 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.20: Contar ejemplares por especie

"""
# Importamos bibliotecas
import copy
import csv
from collections import Counter

# Definimos variables globales
nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
espacio_verde = ["GENERAL PAZ", "ANDES, LOS", "CENTENARIO"]
cantidad_arboles = dict()
lista = []
lista1 = []

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
    
def contar_ejemplares(lista_arboles):
    cadena = ''
    dic = dict()
    
    for i in range(len(lista_arboles)):
        cadena = lista_arboles[i]['nombre_com']
        dic.setdefault(cadena)
        if dic[cadena] == None:
            dic[cadena] = 1
        else:
            dic[cadena] += 1
    
    return dic

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.20: Contar ejemplares por especie.\n')

for i in enumerate(espacio_verde):
    lista = leer_parque(nombre_archivo, i[1])
    cantidad_arboles = contar_ejemplares(lista)
    lista1.append(cantidad_arboles)

for i in lista1:
    print(Counter(i).most_common(5))

#print(f'La lista contiene información de {len(lista)} árboles')
#print(f'La lista de especies en el espacio verde {espacio_verde} contiene {len(especies_presentes)} árboles')

#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.20: Contar ejemplares por especie.

[('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]
[('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]
[('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]

"""