# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 01:05:26 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> solucion_de_errores.py

Determiná los errores de los siguientes códigos y corregilos en un archivo
solucion_de_errores.py comentando brevemente los errores. ¿Qué tipo de errores
tiene cada uno?

"""

#%%
# -> Ejercicio 3.1: Semántica
# -> ¿Anda bien en todos los casos de prueba?

# La ejecución del código planteado no arroja un error al ejecutarlo
# tanto en línea de comandos o como a través de un IDE. El código hace
# distinción de mayúscula y minúscula. Agregué una condición más al if
# para que incluya la mayúscula. Pruebo el código agregando un print
# para visualizar el retorno de la función y agrego un string que no contiene
# la letra a para mostrar que funciona correctamente. En estos casos, que no 
# se necesita distinción de mayusc y minusc es más fácil utilizar algo como:
# if letra in expresion:
#    return True
# Además, la condición else del if hacia que siempre retorne falso.
# la saqué fuera del while.

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.1: Semántica.\n')

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
print(tiene_a('WOLOLO'))


"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.1: Semántica.

True
True
True
False

"""

#%%

# -> Ejercicio 3.2: Sintaxis
# -> ¿Anda bien en todos los casos de prueba?

# No funciona bien. Arroja cinco errores de sintaxis, además que no incluye
# la mayúscula como en el ejercicio anterior.
# El primero, segundo y cuarto se encuentran en que se omitió los dos puntos
# ":", luego de la definición de la función y de las condiciones del while e if
# El tercero en la condición del if, en la que debería ser un comparador "=="
# El quinto error es que escribió en español False (Falso). Corregí agregando
# una condición más en el if para incluir a tanto minúscula como mayúscula.
# Usé los print como en el ejercicio anterior para mostrar que funciona.

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.2: Sintaxis.\n')

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))
print(tiene_a('WOLOLO'))


"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.2: Sintaxis.

True
True

"""

#%%

# -> Ejercicio 3.3: Tipos
# -> ¿Anda bien en todos los casos de prueba?

# Arroja un error porque se introduce un número en vez de una cadena cuando
# se desea obtener el largo de la cadena con la función len().
# Simplemente convierto expresión en tipo string siempre, por si ingresan un
# número en vez de una cadena de caracteres.

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.3: Tipos.\n')

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))


"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.3: Tipos.

False
True
True

"""

#%%

# -> Ejercicio 3.4: Alcances
# -> La siguiente suma no da lo que debería

# La función no retorna ningún valor, por lo tanto la variable c no recibe
# la suma a + b. Simplemente agrego un retorno.

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.4: Alcances.\n')

def suma(a, b):
    return a + b

a = 2
b = 3

c = suma(a, b)

print(f"La suma da {a} + {b} = {c}")


"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.4: Alcances.

La suma da 2 + 3 = 5

"""

#%%

# -> Ejercicio 3.5: Pisando memoria
# -> El siguiente ejemplo usa el dataset de la clase anterior, pero no lo
# -> imprime como corresponde, determinar por qué y explicarlo brevemente.

# El problema se encuentra en que registro se reemplaza constantemente.
# Lo solucioné realizando una copia profunda de registro en la asignación
# de un nuevo dato en la lista.

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.5: Pisando memoria.\n')

import csv
import copy
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(copy.deepcopy(registro))
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)


"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.5: Pisando memoria.

[{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
 {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
 {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
 {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
 {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
 {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]

"""