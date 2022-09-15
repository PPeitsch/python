# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 08:25:44 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.7: La hipoteca de David

David solicitó un crédito a 30 años para comprar una vivienda,
con una tasa fija nominal anual del 5%. Pidió $500000 al banco
y acordó un pago mensual fijo de $2684,11.

"""

print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.7: La hipoteca de David\n')

saldo = input('Ingrese el monto que desea solicitar:')
saldo = int(saldo)

plazo = input('Ingrese el plazo de devolucion:')
plazo = int(plazo)

cuota = 2684.11

tasa = 0.0
if plazo == 30:
    tasa = 0.05

print('La tasa anual sera de:', tasa*100, '%')

pagado = 0.0

while saldo > 0:
    saldo = saldo * (1 + tasa/12) - cuota
    pagado = pagado + cuota

print('El monto total pagado es:', round(pagado, 2))

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.7: La hipoteca de David


Ingrese el monto que desea solicitar:500000

Ingrese el plazo de devolucion:30
La tasa anual sera de: 5.0 %
El monto total pagado es: 966279.6

""" 