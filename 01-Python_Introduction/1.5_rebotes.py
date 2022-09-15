# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 06:25:36 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.5

"""

print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.5\n')

# Lanzamos una pelota desde una altura inicial

altura = 100.0    # en metros
rebote = 0.6      # constante de rebote

for i in range(11):
    print('Altura:', round(altura, 4))
    altura = altura * rebote



"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.5

Altura: 100.0
Altura: 60.0
Altura: 36.0
Altura: 21.6
Altura: 12.96
Altura: 7.776
Altura: 4.6656
Altura: 2.7994
Altura: 1.6796
Altura: 1.0078
Altura: 0.6047

""" 