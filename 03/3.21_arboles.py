# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 07:47:51 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.21: Alturas de una especie en una lista

"""
# Importamos bibliotecas
import copy
import csv
from collections import Counter
import numpy as np

# Definimos variables globales
nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
espacio_verde = ["GENERAL PAZ", "ANDES, LOS", "CENTENARIO"]
cantidad_arboles = dict()
lista = []
lista1 = []
lista2 = []
maximo = [0.00] * len(espacio_verde)
prom = [0.00] * len(espacio_verde)
arbol = 'Jacarandá'

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

def obtener_alturas(lista_arboles, especie):
    lista = []
    altura = 0.00
    
    # Guardo las alturas de los arboles
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            altura = i['altura_tot']
            lista.append(copy.deepcopy(float(altura)))
    
    return lista

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.21: Alturas de una especie en una lista.\n')

for i in enumerate(espacio_verde):
    lista = leer_parque(nombre_archivo, i[1])
    cantidad_arboles = contar_ejemplares(lista)
    lista1.append(cantidad_arboles)
    lista2 = obtener_alturas(lista, arbol)
    prom[i[0]] = round(sum(lista2)/len(lista2), 2)
    maximo[i[0]] = max(lista2)
        

for i in lista1:
    print(Counter(i).most_common(5))

print(f'\nResultados de alturas de {arbol} en los parques:')
for i in range(len(espacio_verde)):
    print(f'{espacio_verde[i]} promedio: {prom[i]} maximo: {maximo[i]}')



#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.21: Alturas de una especie en una lista.

[('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]
[('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]
[('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]

Resultados de alturas de Jacarandá en los parques:
GENERAL PAZ promedio: 10.2 maximo: 16.0
ANDES, LOS promedio: 10.54 maximo: 25.0
CENTENARIO promedio: 8.96 maximo: 18.0

"""