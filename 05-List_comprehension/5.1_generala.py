# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:14:28 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 5.1: Generala servida
Escribí una función tirar() que devuelva una lista con cinco dados generados
aleatoriamente. Escribí otra función llamada es_generala(tirada) que devuelve
True si y sólo si los cinco dados de la lista tirada son iguales.

"""

# Importamos las bibliotecas necesarias
import random

# Definimos variables globales
n_dados = 5         # N° de dados
resultado = False
N = 1000000          # Numero de tiradas

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 5.1: Generala servida.\n')

# Funcion tirada pseudo-random de dados
def tirar():
    tirada = []
    for i in range(n_dados):
        tirada.append(random.randint(1, 6))
    return tirada

# 
def es_generala(tirada):
    contador = False
    resultado = False
    for i in range(len(tirada)-1):
        if tirada[i] == tirada[i+1]:
            contador += 1
    if contador == len(tirada)-1:
        resultado = True
    return resultado

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

#%%
"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio 5.1: Generala servida.

Tiré 1000000 veces, de las cuales 809 saqué generala servida.
Podemos estimar la probabilidad de sacar generala servida mediante 0.000809.

"""