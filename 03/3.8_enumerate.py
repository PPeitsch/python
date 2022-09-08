# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:44:25 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.8: Un ejemplo práctico de enumerate()

Recordá que el archivo Data/missing.csv contiene datos sobre los cajones de
un camión, pero tiene algunas filas que faltan. Usando enumerate(), modificá
tu programa costo_camion.py de forma que imprima un aviso (warning) cada vez
que encuentre una fila incorrecta.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.8: Un ejemplo práctico de enumerate()\n')

# Declaración de variables
precio = 0.00
individual = 0.00

# Abrimos el archivo con el que vamos a trabajar
f = open('../Data/missing.csv', 'rt')
# Guardamos la primera linea, encabezado
headers = next(f).split(',')
# Imprimimos el encabezado
print('El encabezado del archivo es:', headers)

# Recorremos las filas del archivo
for n_fila, fila in enumerate(f, start=1):
    try:
        row = fila.split(',')
        precio += float(row[1].rstrip("\\n")) * float(row[2].rstrip("\\n"))
    except ValueError:
        print(f'Fila {n_fila}: No pude interpretar: {fila}')

# Imprimimos el resultado de la suma total de cajones * precio
print('El precio de todos los cajones es:', round(precio, 2))


# Cerramos el archivo con el que trabajamos
f.close()

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.8: Un ejemplo práctico de enumerate()

El encabezado del archivo es: ['nombre', 'cajones', 'precio\n']
Fila 4: No pude interpretar: Mandarina,,51.23

Fila 7: No pude interpretar: Naranja,,70.44

El precio de todos los cajones es: 30381.15
 
"""