# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:52:52 2021

@author: Pablo Reynoso Peitsch
-> Ejercicio 2.7: Buscar precios

A partir de lo que hiciste en el Ejercicio 2.3, escribí una función
buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de
determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura
en el listado de precios, debe imprimir un mensaje que lo indique.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.7: Buscar precios\n')

# Declaración de variables globales
nombre_archivo = '../Data/precios.csv'
precio = True

with open(nombre_archivo, 'rt', encoding="utf8") as f:
    for line in f:
        row = line.split(',')
        # Imprimimos la lista de frutas
        print(row[0])

def buscar_precio(fruta, nombre_archivo):
    # Declaración de variables locales
    precio = True
    existe = False

    # Abrimos el archivo con el que vamos a trabajar
    f = open('../Data/precios.csv', 'rt', encoding="utf8")
    
    # Recorremos las filas del archivo, buscando la fruta ingresada
    for line in f:
        row = line.split(',')
        if fruta in row[0]:
            precio = float(row[1].rstrip("\\n"))
            existe = True
        elif existe is not True:
            existe = False
    
    # Cerramos el archivo con el que trabajamos
    f.close()
    
    return(precio, existe)


# Ingresamos una palabra por teclado
fruta = input('Ingrese una fruta a buscar: ')

(precio, existe) = buscar_precio(fruta, nombre_archivo)

if existe is True:
    # Imprimimos el precio de la naranja
    print(f'El precio de {fruta} es: {round(precio, 2)}')
else:
    print(f'La fruta ingresada ({fruta}) no se encuentra en la lista.')


# Ingresamos una palabra por teclado
fruta = input('Ingrese otra fruta a buscar: ')

(precio, existe) = buscar_precio(fruta, nombre_archivo)

if existe is True:
    # Imprimimos el precio de la naranja
    print(f'El precio de {fruta} es: {round(precio, 2)}')
else:
    print(f'La fruta ingresada ({fruta}) no se encuentra en la lista.')

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.7: Precio de la naranja

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



Ingrese una fruta a buscar: Frutilla
El precio de Frutilla es: 53.72

Ingrese otra fruta a buscar: Papanoel
La fruta ingresada (Papanoel) no se encuentra en la lista.
 
"""