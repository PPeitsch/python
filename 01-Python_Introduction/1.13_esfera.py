# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 01:22:50 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.13: El volumen de una esfera

En tu directorio de trabajo de esta clase, escribí un programa
llamado esfera.py que le pida al usuario que ingrese por teclado
el radio r de una esfera y calcule e imprima el volumen de la misma.
Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

Finalmente, ejecutá el programa desde la línea de comandos para
responder ¿cuál es el volumen de una esfera de radio 6?

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.13: El volumen de una esfera\n')


# Funciones matemáticas
import math

# Declaración de variables
r = 0.00        # radio de la esfera
v = 0.00        # volumen de la esfera

# Se ingresa por teclado el radio de una esfera
r = input('Por favor ingrese el radio de la esfera: ')
# Se converte la variable r (string actualmente) a tipo flotante
r = float(r)
# Calculo del volumen de la esfera
v = 4/3 * math.pi * r**3

# Impresión del resultado por pantalla
print('El volumen de la esfera es: ', round(v, 2))

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.13: El volumen de una esfera


Por favor ingrese el radio de la esfera: 2.18
El volumen de la esfera es:  43.4

""" 