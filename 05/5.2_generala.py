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
resultado = False
N = 1000          # Numero de tiradas

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio 5.1: Generala servida.\n')

# Funcion tirada pseudo-random de dados
def tirar(n_dados):
    tirada = []
    for i in range(n_dados):
        tirada.append(random.randint(1, 6))
    return tirada

# 
def es_generala(tirada, n_dados):
    contador = False
    resultado = False
    n = False
    while resultado != True and n < 3:
        n += 1
        for i in range(len(tirada)-1):
            if tirada[i] == tirada[i+1]:
                contador += 1
        if contador == len(tirada)-1:
            resultado = True
    return resultado

def prob_generala(N):
    n_dados = 5
    es_generala(tirar(n_dados), n_dados)
    while generala != True and tirada < 3:
        [generala, contador] = es_generala(tirar(n_dados-contador))
        tirada += 1
    G = sum([generala for i in range(N)])
    return G/N

prob = prob_generala(N)

print(f'Tiré {N} veces.')
print(f'La probabilidad de sacar generala servida es {prob:.6f}.')

#%%
"""
RESULTADO:



"""