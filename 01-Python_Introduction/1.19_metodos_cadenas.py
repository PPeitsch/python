# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 07:59:51 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.19: Métodos de cadenas

Experimentá con algunos de los métodos de cadenas introducidos antes.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.19: Métodos de cadenas\n')


# Declaración de variables
frutas = 'Manzana,' 'Naranja,' 'Mandarina,' 'Banana,' 'Kiwi'
minuscula = ''
encontrar = 0

# Impresión de la cadena de texto original
print('\nLa cadena de caracteres original', frutas)

# Pasamos toda la cadena a minusculas
minuscula = frutas.lower()

# Impresión de la cadena de texto en minusculas
print('\nLa cadena de caracteres en minuscula:', minuscula)

# Ingresamos una cadena por teclado
fruta = input('Ingrese una fruta que desee buscar y eliminar: ')

# Buscamos la cadena ingresada en la cadena original
encontrar = minuscula.find(fruta)

if encontrar == -1:
    print('La fruta ingresada no se encuentra en la lista.', encontrar)
else:
    print('La fruta ingresada comienza en la posición:', encontrar)

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.19: Métodos de cadenas


La cadena de caracteres original Manzana,Naranja,Mandarina,Banana,Kiwi

La cadena de caracteres en minuscula: manzana,naranja,mandarina,banana,kiwi

Ingrese una fruta que desee buscar y eliminar: kiwi
La fruta ingresada comienza en la posición: 33

""" 