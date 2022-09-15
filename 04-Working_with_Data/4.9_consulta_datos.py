# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 05:23:55 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 4.9: Consultas de datos
Probá los siguientes ejemplos de consultas (queries) de datos.

"""

# Importamos bibliotecas
import csv
import copy

# Definimos variables globales
nombre_archivo = '../Data/camion.csv'
camion = list()
mas100 = list()
myn = list()
costo10k = list()

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 4.9: Consultas de datos.\n')

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
                print(f'No pude interpretar: {fila}')
    return(lista_temp)

camion = leer_camion(nombre_archivo)

mas100 = [s for s in camion if s['cajones'] > 100]
print(f'Lista con las frutas con mas de 100 cajones: \n{mas100}')
myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]
print(f'Lista de mandarinas y naranjas\n{myn}')
costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
print(f'Lista de costo de frutas mayores a $10.000\n{costo10k}')

#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 4.9: Consultas de datos.

Lista con las frutas con mas de 100 cajones: 
[{'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}]
Lista de mandarinas y naranjas
[{'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]
Lista de costo de frutas mayores a $10.000
[{'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}]

"""