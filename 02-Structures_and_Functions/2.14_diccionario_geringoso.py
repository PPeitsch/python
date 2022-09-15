# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:22:54 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 2.14: Diccionario geringoso.

Construí una función que, a partir de una lista de palabras, devuelva un
diccionario geringoso. Las claves del diccionario deben ser las palabras
de la lista y los valores deben ser sus traducciones al geringoso
(como en el Ejercicio 1.18). Probá tu función para la lista
['banana', 'manzana', 'mandarina']. Guardá este ejercicio en un archivo
diccionario_geringoso.py para entregar al final de la clase.

"""

# Importamos bibliotecas


# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 2.14: Diccionario geringoso.\n')

# Declaración de variables globales
frutas = ['banana', 'manzana', 'mandarina']
lista = ''

def palabra_geringoso(frutas):
    # Declaración de variables locales
    vocales="aeiou"
    lista = frutas
    count = 0
    
    for c in frutas:
        for i in c:
            if i in vocales:
                lista[count] += i + "p" + i
            else:
                lista[count] += i
        count += 1
        #lista = next(lista)
    
    return(lista)

lista = palabra_geringoso(frutas)
print(lista)

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 2.14: Diccionario geringoso.

['bananabapanapanapa', 'manzanamapanzapanapa', 'mandarinamapandaparipinapa']

"""