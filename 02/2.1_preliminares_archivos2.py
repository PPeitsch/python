# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:49:05 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.1: Preliminares sobre lectura de archivos

Corregí el código anterior de forma que el pago del último
mes se ajuste a lo adeudado.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.1: Preliminares sobre lectura de archivos\n')

# Declaración de variables

# Abrimos el archivo con el que vamos a trabajar
f = open('../Data/camion.csv', 'rt')
# Guardamos la primera linea, encabezado
headers = next(f).split(',')
# Imprimimos el encabezado
print('El encabezado del archivo es:', headers)
# Imprimimos todos los datos linea por linea
for line in f:
    row = line.split(',')
    print(row)

# Cerramos el archivo con el que trabajamos
f.close()

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.1: Preliminares sobre lectura de archivos

El encabezado del archivo es: ['nombre', 'cajones', 'precio\n']
['Lima', '100', '32.2\n']
['Naranja', '50', '91.1\n']
['Caqui', '150', '103.44\n']
['Mandarina', '200', '51.23\n']
['Durazno', '95', '40.37\n']
['Mandarina', '50', '65.1\n']
['Naranja', '100', '70.44\n']
 
"""