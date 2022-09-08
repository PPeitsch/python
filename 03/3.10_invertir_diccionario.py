# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 03:38:10 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 3.10: Invertir un diccionario

"""
# Importamos bibliotecas
import csv
import sys

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 3.10: Invertir un diccionario.\n')

# Declaración de variables globales
precios = {}
lista_precios = []
precio = 0.00
fruta = ''

def leer_precios(nombre_archivo):
    # Declaración de variables locales
    lote = {}
    
    # Recorremos las filas del archivo
    with open(nombre_archivo, "rt", encoding="utf-8") as f:
        filas = csv.reader(f)
        for fila in filas:
            try:
                lote[fila[0]] = float(fila[1])
            except IndexError:
                print('En el archivo hay una linea que no contiene datos')
            except ValueError:
                print(f'No pude interpretar: {fila}')
    return(lote)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/precios.csv'
try:
    precios = leer_precios(nombre_archivo)

except FileNotFoundError:
    print('Error: No se encontró el archivo:', nombre_archivo)

# Línea en blanco para separar
print('\n')

# Obtengo las claves del diccionario
precios_items = precios.items()
# Otra forma, por separado items y valores, los cargo en una lista
lista_precios = list(zip(precios.values(), precios.keys()))

# Algunos datos rápidos
# Valor mínimo
print('El precio minimo en la lista es:', min(lista_precios))
# Valor máximo
print('El precio máximo en la lista es:', max(lista_precios))
# Línea en blanco para separar
print('\n')
# Ordeno de menor a mayor
print('El lista de precios ordenada:', sorted(lista_precios))



#%%
"""
RESULTADO :

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 3.10: Invertir un diccionario.

En el archivo hay una linea que no contiene datos


El precio minimo en la lista es: (11.27, 'Cereza')
El precio máximo en la lista es: (106.28, 'Naranja')


El lista de precios ordenada: [(11.27, 'Cereza'), (15.19, 'Ajo'), (15.72, 'Bruselas'), (20.75, 'Remolacha'), (23.16, 'Habas'), (24.22, 'Lechuga'), (24.79, 'Zapallo'), (24.85, 'Uva'), (26.11, 'Radicheta'), (27.58, 'Puerro'), (28.47, 'Berenjena'), (29.26, 'Acelga'), (34.35, 'Frambuesa'), (36.9, 'Rúcula'), (40.22, 'Lima'), (44.85, 'Ciruela'), (49.16, 'Repollo'), (49.74, 'Zanahoria'), (51.94, 'Rabanito'), (52.61, 'Espinaca'), (53.72, 'Frutilla'), (55.16, 'Batata'), (57.1, 'Cebollín'), (58.99, 'Cebolla'), (66.67, 'Tomate'), (69.35, 'Papa'), (73.48, 'Durazno'), (80.89, 'Mandarina'), (105.46, 'Caqui'), (106.28, 'Naranja')]

"""