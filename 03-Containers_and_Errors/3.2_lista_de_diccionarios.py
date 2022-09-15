# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:54:02 2021
Modified on Wed Sep 14 16:21:12 2022

@author: Pablo Reynoso Peitsch

Programación I
-> Ejercicio 3.2: Lista de diccionarios

"""
# Importamos bibliotecas
import csv
import sys
from pprint import pprint
import copy

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación I')
print('Ejercicio 3.2: Lista de diccionarios.\n')

# Declaración de variables globales
lista = []
total = True

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
                print(f'No se puede interpretar: {fila}')
    return(lista_temp)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
try:
    lista = leer_camion(nombre_archivo)

except FileNotFoundError:
    print('Error: No se encontró el archivo:', nombre_archivo)

# Imprimimos el resultado
print('La lista completa es:')
pprint(lista)

for a in range(len(lista)):
    total += lista[a]['cajones'] * lista[a]['precio']

print('El total es: $AR', total)

#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación I
Ejercicio 3.2: Lista de diccionarios.

La lista completa es:
[{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
 {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
 {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
 {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
 {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
 {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]
El total es: $AR 47672.15

"""