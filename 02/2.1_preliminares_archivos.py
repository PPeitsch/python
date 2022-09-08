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
headers = next(f)
# Imprimimos el encabezado
print('El encabezado del archivo es:' ,headers)
# Imprimimos todos los datos linea por linea
for line in f:
    print(line, end = '')

# Cerramos el archivo con el que trabajamos
f.close()

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.1: Preliminares sobre lectura de archivos

El encabezado del archivo es: nombre,cajones,precio

Lima,100,32.2
Naranja,50,91.1
Caqui,150,103.44
Mandarina,200,51.23
Durazno,95,40.37
Mandarina,50,65.1
Naranja,100,70.44
 
"""