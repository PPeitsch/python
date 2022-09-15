# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:03:20 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 4.6: Propagación
Escribí una función llamada propagar que reciba un vector con 0's, 1's y
-1's y devuelva un vector en el que los 1's se propagaron a sus vecinos
con 0. Guardalo en un archivo propaga.py

"""

# Definimos variables globales
lista1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
lista2 = [ 0, 0, 0, 1, 0, 0]
propagada = []

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 4.6: Propagación.\n')

# Funcion para invertir una lista
def propagar(lista):
    propagada = lista.copy()
    propago = False
    
    # Itero sobre la lista
    for h in enumerate(lista):
        if h[1] == 1 and propago == False:
            propago = True
        elif h[1] == 0 and propago == True:
            propagada[h[0]] = 1
        elif h[1] == -1 and propago == True:
            propago = False
    propago = False
    propagada.reverse()
    # Itero sobre la lista en sentido inverso
    for h in enumerate(propagada):
        if h[1] == 1 and propago == False:
            propago = True
        elif h[1] == 0 and propago == True:
            propagada[h[0]] = 1
        elif h[1] == -1 and propago == True:
            propago = False
        #print(h)
    propagada.reverse()
    return propagada

# Invierto la primera lista
propagada = propagar(lista1)

# Imprimo la lista invertida
print(f'La lista:\n{lista1} propagada:\n{propagada}')

# Invierto la segunda lista
propagada = propagar(lista2)

# Imprimo la lista invertida
print(f'\nLa lista:\n{lista2} propagada:\n{propagada}')

#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 4.6: Propagación.

La lista:
[0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0] propagada:
[0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]

La lista:
[0, 0, 0, 1, 0, 0] propagada:
[1, 1, 1, 1, 1, 1]

"""