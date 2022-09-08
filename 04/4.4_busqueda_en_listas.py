# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:09:27 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 4.4: Búsqueda de máximo y mínimo
Agregale a tu archivo busqueda_en_listas.py una función maximo() que busque
el valor máximo de una lista de números positivos.
Si te dan ganas, agregá una función minimo() al archivo.

"""

# Definimos variables globales
lista = [1,2,3,2,3,4]
lista1 = [1,2,3,2,3,4,-3,-4,-9]
lista2 = [-1,-4,-3,-6]
elemento = 0
repeticion = 0
m = 0

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 4.4: Búsqueda de máximo y mínimo.\n')

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

def minimo(lista):
    m = lista[0]
    for e in lista:
        if e>0 and m>e:
            m = e
        elif e<0 and m<abs(e):
            m = e
    return m

def maximo(lista):
    m = lista[0]
    for e in lista:
        if m<e:
            m = e
    return m

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

# Máximo
m = maximo(lista1)
print(f'El máximo número de la lista {lista1} es: {m}')
m = maximo(lista2)
print(f'El máximo número de la lista {lista2} es: {m}')
# Mínimo
m = minimo(lista1)
print(f'El mínimo número de la lista {lista1} es: {m}')
m = minimo(lista2)
print(f'El mínimo número de la lista {lista2} es: {m}')

#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 4.4: Búsqueda de máximo y mínimo.


Ingrese el elemento que desea buscar: 1
La posicion de 1 en la lista es: 0

Ingrese otro elemento que desea buscar: 2
El numero ingresado se encuentra repetido 2 veces
El máximo número de la lista [1, 2, 3, 2, 3, 4, -3, -4, -9] es: 4
El máximo número de la lista [-1, -4, -3, -6] es: -1
El mínimo número de la lista [1, 2, 3, 2, 3, 4, -3, -4, -9] es: -9
El mínimo número de la lista [-1, -4, -3, -6] es: -6

"""