# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:45:26 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.22: Inclinaciones por especie de una lista

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
lista2 = []
lista3 = []
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

def obtener_inclinaciones(lista_arboles, especie):
    lista = []
    inclinacion = 0
    
    # Guardo las alturas de los arboles
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            inclinacion = i['inclinacio']
            lista.append(copy.deepcopy(int(inclinacion)))
    
    return lista

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.22: Inclinaciones por especie de una lista.\n')

for i in enumerate(espacio_verde):
    lista = leer_parque(nombre_archivo, i[1])
    cantidad_arboles = contar_ejemplares(lista)
    lista1.append(cantidad_arboles)
    lista2 = obtener_alturas(lista, arbol)
    lista3 = obtener_inclinaciones(lista, arbol)
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



"""