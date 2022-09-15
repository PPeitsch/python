# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 01:52:29 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.15: Concatenación de cadenas

A pesar de ser sólo de lectura, siempre podés reasignar una variable
a una cadena nueva. Probá el siguiente comando que concatena la palabra
"Pera" al final de frutas

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.15: Concatenación de cadenas\n')


# Declaración de variables
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'
nueva_fruta = ''

# Imprimimos el resultado
print('La cadena de caracteres original es:\n', frutas)

# Ingreso de una fruta nueva por teclado
nueva_fruta = input('Ingrese una fruta para agregar al final de la cadena: ')

# Concatenación de strings al final de una cadena
frutas = frutas + ',' + nueva_fruta

# Imprimimos el resultado
print('La cadena ahora es:\n', frutas)

# Ingreso de una fruta nueva por teclado
nueva_fruta = input('Ingrese una fruta para agregar al principio de la cadena: ')

# Concatenación de strings al principio de una cadena
frutas = nueva_fruta + ',' + frutas

# Imprimimos el resultado
print('La cadena ahora es:\n', frutas)

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.15: Concatenación de cadenas

La cadena de caracteres original es:
 Manzana,Naranja,Mandarina,Banana,Kiwi

Ingrese una fruta para agregar al final de la cadena: Pomelo
La cadena ahora es:
 Manzana,Naranja,Mandarina,Banana,Kiwi,Pomelo

Ingrese una fruta para agregar al principio de la cadena: Melon
La cadena ahora es:
 Melon,Manzana,Naranja,Mandarina,Banana,Kiwi,Pomelo

""" 