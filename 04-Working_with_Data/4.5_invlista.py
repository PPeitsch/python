# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:24:40 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 4.5: Invertir una lista
Escribí una función invertir_lista(lista) que dada una lista devuelva otra
que tenga los mismos elementos pero en el orden inverso. Es decir, el que era
el primer elemento de la lista de entrada deberá ser el último de la lista
de salida y análogamente con los demás elementos.

"""

# Definimos variables globales
lista1 = [1, 2, 3, 4, 5]
lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
invertida = []

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 4.5: Invertir una lista.\n')

# Funcion para invertir una lista
def invertir_lista(lista):
    invertida = []
    # Itero sobre la lista
    for e in reversed(lista):
        invertida.append(e)
    return invertida

# Invierto la primera lista
invertida = invertir_lista(lista1)

# Imprimo la lista invertida
print(f'La lista:\n{lista1} invertida:\n{invertida}')

# Invierto la segunda lista
invertida = invertir_lista(lista2)

# Imprimo la lista invertida
print(f'\nLa lista:\n{lista2} invertida:\n{invertida}')

#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 4.5: Invertir una lista.

La lista:
[1, 2, 3, 4, 5] invertida:
[5, 4, 3, 2, 1]

La lista:
['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'] invertida:
['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']

"""