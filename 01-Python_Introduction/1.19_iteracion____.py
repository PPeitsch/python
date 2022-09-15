# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 01:52:29 2021

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
cadena = "Ejemplo con for"
contador1 = 0
contador2 = 0

for c in cadena:
    contador1 += 1
    print('Caracter:', c, '\tPosicion: ', contador1)
    if c == 'o':
        contador2 += 1

# Impresión cantidad de letras
print('\nLa cantidad de letras es:', contador2)
        

"""
RESULTADO:



""" 