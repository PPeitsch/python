# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:43:19 2021

@author: Pablo Reynoso Peitsch
-> Ejercicio 2.3: Precio de la naranja

Escribí un código que abra el archivo Data/precios.csv,
busque el precio de la naranja y lo imprima en pantalla.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.3: Precio de la naranja\n')

# Declaración de variables
precio = 0.00

with open('../Data/precios.csv', 'rt', encoding="utf8") as f:
    for line in f:
        row = line.split(',')
        # Imprimimos la lista de frutas
        print(row[0])

# Ingresamos una palabra por teclado
fruta = input('Ingrese una fruta a buscar: ')

# Abrimos el archivo con el que vamos a trabajar
f = open('../Data/precios.csv', 'rt', encoding="utf8")

# Recorremos las filas del archivo, buscando la fruta ingresada
for line in f:
    row = line.split(',')
    if fruta in row[0]:
        precio = float(row[1].rstrip("\\n"))


# Imprimimos el precio de la naranja
print(f'El precio de {fruta} es: {round(precio, 2)}')


# Cerramos el archivo con el que trabajamos
f.close()

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.3: Precio de la naranja

Lima
Uva
Ciruela
Cereza
Frutilla
Caqui
Tomate
Berenjena
Lechuga
Durazno
Remolacha
Habas
Frambuesa
Naranja
Bruselas
Batata
Rúcula
Radicheta
Repollo
Cebolla
Cebollín
Puerro
Mandarina
Ajo
Rabanito
Zapallo
Espinaca
Acelga
Zanahoria
Papa



Ingrese una fruta a buscar: Rúcula
El precio de Rúcula es: 36.9
 
"""