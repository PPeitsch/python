# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 05:01:59 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 4.7: Comprensión de listas
Probá un par de comprensión de listas para familiarizarte con la sintaxis.

"""

# Definimos variables globales
nums = [1, 2, 3, 4]

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 4.7: Comprensión de listas.\n')

# Obtengo el cuadrado de los numeros en la lista
cuadrados = [x*x for x in nums]
# Imprimo la lista invertida
print(f'La lista:\n{nums} \n al cuadrado es:\n{cuadrados}')

# Obtengo el doble de los numeros de la lista, si son mayores que 2
dobles = [2*x for x in nums if x>2]
# Imprimo la lista invertida
print(f'\nLos números de la lista:\n{nums} \n multiplicados por 2 son y si son mayores a 2:\n{dobles}')


#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 4.7: Comprensión de listas.

La lista:
[1, 2, 3, 4] 
 al cuadrado es:
[1, 4, 9, 16]

Los números de la lista:
[1, 2, 3, 4] 
 multiplicados por 2 son y si son mayores a 2:
[6, 8]

"""