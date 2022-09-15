# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 03:06:39 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.6: Contar

"""
# Importamos bibliotecas

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.6: Contar\n')

# Cuenta hasta el 10
for n in range(10):
    print(n, end=' ')
print('\n')

# Cuenta del 10 al 0
for n in range(10,0,-1):
    print(n, end=' ')
print('\n')

# Cuenta números pares, del 0 al 10
for n in range(0,10,2):
    print(n, end=' ')
print('\n')


#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.6: Contar

0 1 2 3 4 5 6 7 8 9 

10 9 8 7 6 5 4 3 2 1 

0 2 4 6 8 

"""