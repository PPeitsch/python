# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:51:23 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.23: Especie con el ejemplar más inclinado

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
mas_inclinado =  dict()
mayor_inclinacion = [0] * len(espacio_verde)

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

def especimen_mas_inclinado(lista_arboles):
    inclinacion = []
    mayor_inclinacion = 0
    dic = dict()
    
    for i in especies(lista_arboles):
        inclinacion = obtener_inclinaciones(lista_arboles, i)
        mayor_inclinacion = max(inclinacion)
        dic.setdefault(i)
        dic[i] =  mayor_inclinacion
    #inclinaciones.append(copy.deepcopy(dic))+
    mayor_inclinacion = max(dic, key=lambda key: dic[key])
    
    return dic

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.23: Especie con el ejemplar más inclinado.\n')

for i in enumerate(espacio_verde):
    lista = leer_parque(nombre_archivo, i[1])
    cantidad_arboles = contar_ejemplares(lista)
    lista1.append(cantidad_arboles)
    lista2 = obtener_alturas(lista, arbol)
    
    mas_inclinado = especimen_mas_inclinado(lista)
    mayor_inclinacion[i[0]] = max(mas_inclinado, key=lambda key: mas_inclinado[key])
    lista3.append(copy.deepcopy(mas_inclinado))
    
    prom[i[0]] = round(sum(lista2)/len(lista2), 2)
    maximo[i[0]] = max(lista2)

for i in lista1:
    print(Counter(i).most_common(5))

print(f'\nResultados de alturas de {arbol} en los parques:')
for i in range(len(espacio_verde)):
    print(f'{espacio_verde[i]} promedio: {prom[i]} maximo: {maximo[i]}')

print('\nResultados de las mayores inclinaciones de arboles en los parques:')
for i in range(len(espacio_verde)):
    print(f'En {espacio_verde[i]} es: {mayor_inclinacion[i]}, con una inclinación de: {lista3[i][mayor_inclinacion[i]]} grados')



#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.23: Especie con el ejemplar más inclinado.

[('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]
[('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]
[('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]

Resultados de alturas de Jacarandá en los parques:
GENERAL PAZ promedio: 10.2 maximo: 16.0
ANDES, LOS promedio: 10.54 maximo: 25.0
CENTENARIO promedio: 8.96 maximo: 18.0

Resultados de las mayores inclinaciones de arboles en los parques:
En GENERAL PAZ es: Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert), con una inclinación de: 70 grados
En ANDES, LOS es: Jacarandá, con una inclinación de: 30 grados
En CENTENARIO es: Falso Guayabo (Guayaba del Brasil), con una inclinación de: 80 grados

"""