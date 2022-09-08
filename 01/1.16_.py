# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 01:52:29 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.16: Testeo de pertenencia

Experimentá con el operador in para buscar subcadenas.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.16: Testeo de pertenencia\n')


# Declaración de variables
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'
nueva_fruta = ''
buscar_fruta = ''

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

# Ingreso por teclado de una fruta a buscar
buscar_fruta = input('Ingrese una fruta a buscar: ')

# Testeo de pertenencia
if buscar_fruta in frutas:
    print('La fruta se encuentra en la cadena.')
else:
    print('No se encuentra')

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.16: Testeo de pertenencia

La cadena de caracteres original es:
 Manzana,Naranja,Mandarina,Banana,Kiwi

Ingrese una fruta para agregar al final de la cadena: Maracuya
La cadena ahora es:
 Manzana,Naranja,Mandarina,Banana,Kiwi,Maracuya

Ingrese una fruta para agregar al principio de la cadena: Anana
La cadena ahora es:
 Anana,Manzana,Naranja,Mandarina,Banana,Kiwi,Maracuya

Ingrese una fruta a buscar: Lima
No se encuentra

""" 