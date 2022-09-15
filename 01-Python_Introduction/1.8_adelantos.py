# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:15:00 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.8: La hipoteca de David - Adelantos

David solicitó un crédito a 30 años para comprar una vivienda,
con una tasa fija nominal anual del 5%. Pidió $500000 al banco
y acordó un pago mensual fijo de $2684,11.

Supongamos que David adelanta pagos extra de $1000/mes durante
los primeros 12 meses de la hipoteca.
Modificá el programa para incorporar estos pagos extra y que 
imprima el monto total pagado junto con la cantidad de meses requeridos.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.8: La hipoteca de David - Adelantos\n')

# Declaración de variables
i = 0
tasa = 0.0
pagado = 0.0

# Monto del préstamo
saldo = input('Ingrese el monto que desea solicitar: ')
# Convierto el string a entero
saldo = int(saldo)

# Plazo de devolución, en años
plazo = input('Ingrese el plazo, en años, de devolucion: ')
# Convierto el string ingresado en entero
plazo = int(plazo)

if plazo == 30:
    tasa = 0.05

# Valor de la cuota fija, según el interés
cuota = 2684.11

# Informo el % de tasa anual
print('La tasa anual sera de:', tasa*100, '%')

# Pregunto el monto de cada adelanto mensual
adelanto = input('Cual es el monto mensual a adelantar? ')
# Convierto el string ingresado en entero
adelanto = int(adelanto)

# Durante cuantas cuotas va a realizar el adelanto
cuotas_adelanto = input('Durante cuantas cuotas? ')
# Convierto el string ingresado en entero
cuotas_adelanto = int(cuotas_adelanto)

# Calculo de costo final descontando los daelantos
while saldo > 0:
    saldo = saldo * (1 + tasa/12) - cuota
    pagado = pagado + cuota
    i += 1
    
    if i <= cuotas_adelanto:
        saldo = saldo - adelanto
        pagado = pagado + adelanto

print('El monto total pagado es:', round(pagado, 2))
print('En un total de', i, 'meses')

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.8: La hipoteca de David - Adelantos


Ingrese el monto que desea solicitar: 500000

Ingrese el plazo, en años, de devolucion: 30
La tasa anual sera de: 5.0 %

Cual es el monto mensual a adelantar? 1000

Durante cuantas cuotas? 12
El monto total pagado es: 929965.62
En un total de 342 meses

""" 