# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 08:39:39 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.20: f-strings

A veces querés crear una cadena que incorpore los valores de otras
variables en ella. Para hacer eso, usá una f-string

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.20: f-strings\n')


# Declaración de variables
frutas = ('manzana', 'naranja', 'mandarina', 'banana', 'kiwi')
cajones = (100, 20, 0, 4, 80)
precio = (150.05, 98.46, 76.00, 99.99, 249.89)

# Impresión de la cadena de texto original
print('\nLas cadenas de caracteres originales: \n')
print(frutas, '\n', cajones, '\n', precio, '\n')

# Otra forma de imprimir el array de strings
print(f'{cajones}\n cajones de {frutas}\n a ${precio:}\n')


"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.20: f-strings


Las cadenas de caracteres originales: 

('manzana', 'naranja', 'mandarina', 'banana', 'kiwi') 
 (100, 20, 0, 4, 80) 
 (150.05, 98.46, 76.0, 99.99, 249.89) 

(100, 20, 0, 4, 80)
 cajones de ('manzana', 'naranja', 'mandarina', 'banana', 'kiwi')
 a $(150.05, 98.46, 76.0, 99.99, 249.89)

""" 