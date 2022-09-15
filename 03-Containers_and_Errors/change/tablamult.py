# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 02:23:14 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.17: Tablas de multiplicar
Escribí un programa tablamult.py que imprima de forma prolija las tablas de
multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la
multiplicación, usando sólo sumas alcanza.

"""
# Importamos bibliotecas
import copy

# Definimos variables globales
n = [i for i in range(10)]
lista = []

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.17: Tablas de multiplicar.\n')

def tabla(n):
    lista = []
    suma = {}
    
    for i in range(len(n)):
        for j in range(len(n)):
            suma[j] = i*j
        lista.append(copy.deepcopy(suma))
    
    return lista

# Imprimo encabezado
#print(f'      {n[0]:>2d}  {n[1]:>2d}  {n[2]:>2d}  {n[3]:>2d}  {n[4]:>2d}  {n[5]:>2d}  {n[6]:>2d}  {n[7]:>2d}  {n[8]:>2d}  {n[9]:>2d}')
print('    ', end=' ')
for i in range(len(n)):
    print(' ', i, end=' ')
lista = tabla(n)
# Imprimo linea separadora
print('\n---------------------------------------------')

for i in range(len(lista)):
    print(f'{n[i]:>2d}: ', end='')
    for j in range(len(lista)):
        print(f'  {lista[i][j]:>2d}', end='')
    print('')




#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.17: Tablas de multiplicar.

       0   1   2   3   4   5   6   7   8   9 
---------------------------------------------
 0:    0   0   0   0   0   0   0   0   0   0
 1:    0   1   2   3   4   5   6   7   8   9
 2:    0   2   4   6   8  10  12  14  16  18
 3:    0   3   6   9  12  15  18  21  24  27
 4:    0   4   8  12  16  20  24  28  32  36
 5:    0   5  10  15  20  25  30  35  40  45
 6:    0   6  12  18  24  30  36  42  48  54
 7:    0   7  14  21  28  35  42  49  56  63
 8:    0   8  16  24  32  40  48  56  64  72
 9:    0   9  18  27  36  45  54  63  72  81

"""