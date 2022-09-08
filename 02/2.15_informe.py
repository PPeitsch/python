# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:54:02 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.15: Lista de tuplas

"""
# Importamos bibliotecas
import csv
import sys
from pprint import pprint

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.15: Lista de tuplas.\n')

# Declaración de variables globales
lista = []
total = True

def leer_camion(nombre_archivo):
    # Declaración de variables locales
    lista_temp = []
    lote = ()
    
    # Recorremos las filas del archivo
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        print(encabezado)
        for fila in filas:
            try:
                fruta = fila[0]
                n_cajones = int(fila[1])
                precio = float(fila[2])
                lote = (fruta, n_cajones, precio)
                lista_temp.append(lote)
            except ValueError:
                print(f'No pude interpretar: {fila}')
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
    total += lista[a][1] * lista[a][2]

print('El total es:', total)

#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.15: Lista de tuplas.

['nombre', 'cajones', 'precio']
La lista completa es:
[('Lima', 100, 32.2),
 ('Naranja', 50, 91.1),
 ('Caqui', 150, 103.44),
 ('Mandarina', 200, 51.23),
 ('Durazno', 95, 40.37),
 ('Mandarina', 50, 65.1),
 ('Naranja', 100, 70.44)]
El total es: 47672.15

"""