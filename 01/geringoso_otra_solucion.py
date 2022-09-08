# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 08:28:28 2021

@author: Pablo Reynoso Peitsch
"""
# Ingreso por teclado de una palabra
cadena = input('Por favor, ingrese la palabra que desea pasar a geringoso: ')
geringoso = cadena
geringoso = geringoso.replace('a', 'apa')
geringoso = geringoso.replace('e', 'epe')
geringoso = geringoso.replace('i', 'ipi')
geringoso = geringoso.replace('o', 'opo')
geringoso = geringoso.replace('u', 'upu')
print ('El resultado es:', geringoso)