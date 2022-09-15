# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:43:19 2021

@author: Pablo Reynoso Peitsch
-> Ejercicio 2.4: Archivos comprimidos

¿Que pasaría si quisiéramos leer un archivo comprimido con gzip, por ejemplo?
La función primitiva de Python open() no hace esa tarea. Pero hay un módulo
de la biblioteca de Python llamado gzip que lee archivos comprimidos.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.4: Archivos comprimidos\n')

# Importamos bibliotecas
import gzip

# Declaración de variables
precio = 0.00

with gzip.open('../Data/camion.csv.gz', 'rt', encoding="utf8") as f:
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        # Imprimimos la lista de frutas
        print(row[0])


# Abrimos el archivo con el que vamos a trabajar
f = gzip.open('../Data/camion.csv.gz', 'rt', encoding="utf8")
# Guardamos la primera linea, encabezado
headers = next(f).split(',')
# Imprimimos el encabezado
print('\nEl encabezado del archivo es:', headers)


# Ingresamos una palabra por teclado
fruta = input('Ingrese una fruta a buscar: ')

# Recorremos las filas del archivo, buscando la fruta ingresada
for line in f:
    row = line.split(',')
    if fruta in row[0]:
        precio = float(row[2].rstrip("\\n"))


# Imprimimos el precio de la naranja
print(f'El precio de {fruta} es: {round(precio, 2)}')


# Cerramos el archivo con el que trabajamos
f.close()

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.4: Archivos comprimidos

Lima
Naranja
Caqui
Mandarina
Durazno
Mandarina
Naranja

El encabezado del archivo es: ['nombre', 'cajones', 'precio\n']

Ingrese una fruta a buscar: Lima
El precio de Lima es: 32.2
 
"""