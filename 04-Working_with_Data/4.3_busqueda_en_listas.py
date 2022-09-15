# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:38:58 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 4.3: Búsquedas de un elemento
Creá el archivo busqueda_en_listas.py para guardar tu código de este ejercicio
y el siguiente. En este primer ejercicio tenés que escribir una función
buscar_u_elemento() que reciba una lista y un elemento y devuelva la posición
de la última aparición de ese elemento en la lista (o -1 si el elemento no
pertenece a la lista).
Agregale a tu programa busqueda_en_listas.py una función buscar_n_elemento()
que reciba una lista y un elemento y devuelva la cantidad de veces que aparece
el elemento en la lista.

"""

# Definimos variables globales
lista = [1,2,3,2,3,4]
elemento = 0
repeticion = 0

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 4.3: Búsquedas de un elemento.\n')

def buscar_u_elemento(lista, elemento):
    # Definimos variables locales
    posicion = -1
    
    for i in enumerate(lista):
        if i[1] == elemento:
            posicion = i[0]
    
    return(posicion)

def buscar_n_elemento(lista, elemento):
    # Definimos variables locales
    repeticion = 0
    
    for i in enumerate(lista):
        if i[1] == elemento:
            repeticion += 1
    
    return(repeticion)

# Buscamos un elemento ingresado por teclado
elemento = input('Ingrese el elemento que desea buscar: ')
elemento = int(elemento)

posicion = buscar_u_elemento(lista, elemento)

if posicion == -1:
    print(f'No se encontró {elemento} en la lista.')
else:
    print(f'La posicion de {elemento} en la lista es: {posicion}')

# Buscamos un elemento ingresado por teclado
elemento = input('Ingrese otro elemento que desea buscar: ')
elemento = int(elemento)

repeticion = buscar_n_elemento(lista, elemento)

print(f'El numero ingresado se encuentra repetido {repeticion} veces')

#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 4.3: Búsquedas de un elemento.


Ingrese el elemento que desea buscar: 4
La posicion de 4 en la lista es: 5

Ingrese otro elemento que desea buscar: 3
El numero ingresado se encuentra repetido 2 veces

"""