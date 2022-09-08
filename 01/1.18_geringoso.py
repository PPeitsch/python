# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 07:58:23 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.18: Geringoso rústico

Usá una iteración sobre el string cadena para agregar la sílaba
'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
Podés probar tu código cambiando la cadena inicial por otra palabra,
como 'apa' o 'boligoma'.

Guardá el código en un archivo geringoso.py.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.18: Geringoso rústico\n')

# Declaración de variables
geringoso = ''

# Ingreso por teclado de una palabra
cadena = input('Por favor, ingrese la palabra que desea pasar a geringoso: ')


# Cadena en geringoso
for c in cadena:
    if c == 'a':
        c += 'pa'
        print(c)
    elif c == 'e':
        c += 'pe'
        print(c)
    elif c == 'i':
        c += 'pi'
        print(c)
    elif c == 'o':
        c += 'po'
        print(c)
    elif c == 'u':
        c += 'pu'
        print(c)
    geringoso += c

# Impresión del resultado
print('En geringoso, la palabra introducida es:', geringoso)


"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.18: Geringoso rústico


Por favor, ingrese la palabra que desea pasar a geringoso: caleidoscopio
En geringoso, la palabra introducida es: capalepeipidoposcopopipiopo

""" 